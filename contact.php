<?php
/**
 * Laybond – contact form handler (works on any cPanel / PHP hosting)
 * -------------------------------------------------------------------
 * CHANGE THESE IF NEEDED:
 */
$TO_EMAIL   = 'sales@laybond.co.in';          // where enquiries are delivered
$CC_EMAIL   = 'laybond@gmail.com';            // optional copy ('' to disable)
$FROM_EMAIL = 'no-reply@laybond.co.in';       // must be an address on YOUR domain for good deliverability
$SUBJECT    = 'New website enquiry – Laybond';
/* ------------------------------------------------------------------- */

header('X-Content-Type-Options: nosniff');
$isAjax = isset($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'fetch';

function respond($ok, $error = '') {
    global $isAjax;
    if ($isAjax) {
        header('Content-Type: application/json; charset=utf-8');
        if (!$ok) http_response_code(400);
        echo json_encode(['ok' => $ok, 'error' => $error]);
    } else {
        header('Location: ' . ($ok ? 'thank-you.html' : 'contact.html?error=1'));
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') respond(false, 'Invalid request.');

// Spam checks: honeypot field must be empty, and the form must not be submitted instantly
if (!empty($_POST['website'])) respond(true);
$ts = isset($_POST['ts']) ? (int) $_POST['ts'] : 0;
if ($ts > 0 && (round(microtime(true) * 1000) - $ts) < 3000) respond(false, 'Please wait a moment and try again.');

function clean($key, $max = 200) {
    $v = isset($_POST[$key]) ? trim((string) $_POST[$key]) : '';
    $v = str_replace(["\r", "\n", "%0a", "%0d"], ' ', $v);   // block header injection
    return mb_substr(strip_tags($v), 0, $max);
}

$name    = clean('name', 100);
$company = clean('company', 150);
$phone   = clean('phone', 30);
$email   = clean('email', 150);
$product = clean('product', 100);
$message = isset($_POST['message']) ? mb_substr(strip_tags(trim((string) $_POST['message'])), 0, 5000) : '';

if ($name === '' || $message === '') respond(false, 'Please fill in your name and requirement.');
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) respond(false, 'Please enter a valid email address.');
if (strlen(preg_replace('/\D/', '', $phone)) < 10) respond(false, 'Please enter a valid phone number.');
if (preg_match_all('/https?:\/\//i', $message) > 3) respond(false, 'Too many links in message.');

$body  = "New enquiry from laybond.co.in\n";
$body .= "==============================\n\n";
$body .= "Name:     $name\n";
$body .= "Company:  " . ($company ?: '-') . "\n";
$body .= "Phone:    $phone\n";
$body .= "Email:    $email\n";
$body .= "Product:  " . ($product ?: '-') . "\n\n";
$body .= "Requirement:\n$message\n\n";
$body .= "------------------------------\n";
$body .= "Sent: " . date('d M Y, H:i') . " | IP: " . ($_SERVER['REMOTE_ADDR'] ?? '') . "\n";

$headers   = [];
$headers[] = 'From: Laybond Website <' . $FROM_EMAIL . '>';
$headers[] = 'Reply-To: ' . $name . ' <' . $email . '>';
if ($CC_EMAIL) $headers[] = 'Cc: ' . $CC_EMAIL;
$headers[] = 'MIME-Version: 1.0';
$headers[] = 'Content-Type: text/plain; charset=UTF-8';
$headers[] = 'X-Mailer: PHP/' . phpversion();

$subject = '=?UTF-8?B?' . base64_encode($SUBJECT . ($product ? " ($product)" : '')) . '?=';
$sent = @mail($TO_EMAIL, $subject, $body, implode("\r\n", $headers), '-f' . $FROM_EMAIL);

respond($sent, $sent ? '' : 'Sorry, the message could not be sent. Please call +91 94431 69842 or email sales@laybond.co.in.');
