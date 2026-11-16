# Deploying the new Laybond website (cPanel)

## What's in this folder
| Item | Purpose |
|---|---|
| `*.html` | The 15 pages. Old page names are kept so Google links keep working |
| `contact.php` | Sends the contact form to sales@laybond.co.in |
| `assets/` | CSS, JavaScript, images, videos, PDFs |
| `.htaccess` | HTTPS redirect, caching, compression, custom 404 (hidden file) |
| `sitemap.xml`, `robots.txt` | For Google |
| `_dev/` | Page generator used to build the site. **Not needed online**; don't upload |
| `MEDIA-GUIDE.md`, `README-DEPLOY.md` | These notes. No need to upload |

## Steps
1. **Back up the old site.** In cPanel → File Manager → `public_html` → select all → *Compress* → download the zip.
2. Add your photos and videos per `MEDIA-GUIDE.md` (you can also do this later).
3. In `public_html`, delete the old site's files: the old `.html` pages and the old `images/` folder.
   *Exception:* if anything links directly to the old PDFs (e.g. `images/pdf/...`), they are redirected automatically to the new location by .htaccess.
4. Upload everything in this folder **except `_dev/` and the .md files** into `public_html`.
   - Easiest: zip the files on your Mac, upload the zip, then use *Extract* in File Manager.
   - Make sure `.htaccess` is uploaded. It's hidden on Mac; press **Cmd + Shift + .** in Finder to show it.
5. **Contact form email:** open `contact.php` and check the three lines at the top:
   - `$TO_EMAIL` – where enquiries go (sales@laybond.co.in)
   - `$CC_EMAIL` – a copy (laybond@gmail.com), or `''` for none
   - `$FROM_EMAIL` – must be an address on laybond.co.in. Create `no-reply@laybond.co.in` in cPanel → Email Accounts if mail doesn't arrive.
6. Visit https://laybond.co.in, send a test enquiry from the Contact page, and check the inbox (and spam folder).
7. Google: in Google Search Console, submit `https://laybond.co.in/sitemap.xml`.

## Troubleshooting
- **Form says "could not be sent":** your host may block PHP `mail()`. Ask the host to enable it, or ask for an SMTP version of contact.php.
- **Site shows the www / http version:** `.htaccess` wasn't uploaded, or `mod_rewrite` is off. Check with your host.
- **HTTPS error:** enable the free AutoSSL / Let's Encrypt certificate in cPanel → SSL/TLS Status.
- **Images not appearing:** check the filename matches exactly (lowercase, `.jpg`).

## Editing text later
Each page is plain HTML. Open it in any editor (VS Code is free), find the text and change it.
The header and footer are repeated in every page; for site-wide changes, either edit all pages
(search & replace across files) or regenerate with the script in `_dev/` (`python3 _dev/build.py .`).
