/* ==========================================================================
   GALLERY LIST — edit this file to add or remove photos and videos.

   To add a photo:
     1. Copy the image into  assets/images/gallery/   (JPG or WebP, ~1600px wide)
     2. Add a line below, e.g.
        { src: "assets/images/gallery/my-photo.jpg", title: "40 m³ HCl tank", category: "tanks" },

   To add a video:
     1. Copy the MP4 into  assets/videos/   and a still frame into assets/images/gallery/
     2. Add (videos show a play button):
        { type: "video", src: "assets/videos/my-clip.mp4", poster: "assets/images/gallery/my-clip.jpg",
          title: "Site installation", category: "site" },

   Categories (must match the filter buttons on gallery.html):
     tanks · acid · scrubbers · piping · linings · fabrication · site
   Optional extras:  wide: true  (double-width tile)   featured: true  (shows on Home page)
   ========================================================================== */
window.LAYBOND_GALLERY = [
  { src: "assets/images/gallery/tanks-01.jpg", title: "FRP chemical storage tank with ladder & platform", category: "tanks", categoryLabel: "Tanks & Vessels", featured: true, wide: true },
  { src: "assets/images/gallery/acid-01.jpg", title: "Acid storage & dosing system with safety rails", category: "acid", categoryLabel: "Acid Handling", featured: true },
  { src: "assets/images/gallery/scrubber-01.jpg", title: "FRP fume scrubber towers & stacks", category: "scrubbers", categoryLabel: "Scrubbing Systems", featured: true },
  { src: "assets/images/gallery/piping-01.jpg", title: "Flanged pipe spools ready for dispatch", category: "piping", categoryLabel: "Pipe & Fittings", featured: true },
  { src: "assets/images/gallery/lining-01.jpg", title: "Clarifier lining – concrete protection", category: "linings", categoryLabel: "Linings", featured: true },
  { src: "assets/images/gallery/fabrication-01.jpg", title: "Pressure vessels & interconnecting piping", category: "fabrication", categoryLabel: "Fabrication", featured: true },
  { src: "assets/images/gallery/site-01.jpg", title: "Site installation team at work", category: "site", categoryLabel: "Site Work", wide: true },
  { src: "assets/images/gallery/tanks-02.jpg", title: "Horizontal FRP storage tank", category: "tanks", categoryLabel: "Tanks & Vessels" },
  { src: "assets/images/gallery/tanks-03.jpg", title: "Large FRP tank with manway", category: "tanks", categoryLabel: "Tanks & Vessels" },
  { src: "assets/images/gallery/acid-02.jpg", title: "Chemical dosing tanks & pump skid", category: "acid", categoryLabel: "Acid Handling" },
  { src: "assets/images/gallery/scrubber-02.jpg", title: "Scrubber with blue FRP ducting", category: "scrubbers", categoryLabel: "Scrubbing Systems" },
  { src: "assets/images/gallery/piping-02.jpg", title: "Large-bore FRP flanged pipe", category: "piping", categoryLabel: "Pipe & Fittings" },
  { src: "assets/images/gallery/factory-01.jpg", title: "Laybond works, SIPCOT Pudukkottai", category: "site", categoryLabel: "Site Work" },
  { src: "assets/images/gallery/lining-02.jpg", title: "Pit lining in progress", category: "linings", categoryLabel: "Linings" },
  { src: "assets/images/gallery/fabrication-02.jpg", title: "FRP motor guard canopies", category: "fabrication", categoryLabel: "Fabrication" },
  { src: "assets/images/gallery/site-02.jpg", title: "Lifting a finished FRP tank", category: "site", categoryLabel: "Site Work", wide: true },
  { src: "assets/images/gallery/tanks-04.jpg", title: "20 KL HCl bulk storage tank", category: "tanks", categoryLabel: "Tanks & Vessels" },
  { src: "assets/images/gallery/tanks-05.jpg", title: "Horizontal tank on concrete saddles", category: "tanks", categoryLabel: "Tanks & Vessels" },
  { src: "assets/images/gallery/site-03.jpg", title: "FRP tanks loaded for delivery", category: "site", categoryLabel: "Site Work" },
  { src: "assets/images/gallery/scrubber-03.jpg", title: "Fume extraction column", category: "scrubbers", categoryLabel: "Scrubbing Systems" },
  { src: "assets/images/gallery/lining-03.jpg", title: "Interior tank lining application", category: "linings", categoryLabel: "Linings" },
  { src: "assets/images/gallery/fabrication-03.jpg", title: "Large vessel shell fabrication", category: "fabrication", categoryLabel: "Fabrication" },
  { src: "assets/images/gallery/acid-03.jpg", title: "Dosing pump & valve assembly", category: "acid", categoryLabel: "Acid Handling" },
  { src: "assets/images/gallery/tanks-06.jpg", title: "Green FRP tanks at site", category: "tanks", categoryLabel: "Tanks & Vessels" }
];
