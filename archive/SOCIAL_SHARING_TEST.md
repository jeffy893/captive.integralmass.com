# Social Sharing Test Guide

## Quick Reference for Testing Logo Display

### ✅ What Was Fixed

1. **Open Graph Meta Tags** - Added to all 4 HTML pages
2. **Twitter Card Meta Tags** - Added to all 4 HTML pages  
3. **Favicon** - Added to all 4 HTML pages
4. **Logo File** - Located at `docs/assets/captive-iMASS-logo.png` (1.9MB)
5. **Brand Bar Link Color** - Changed to sky blue (#87CEEB) for visibility

---

## Testing on Your Phone

### Method 1: SMS/iMessage (iPhone)
1. Open Messages app
2. Create new message
3. Paste link: `https://captive.integralmass.com/`
4. **Expected Result**: Logo preview appears above link

### Method 2: WhatsApp
1. Open WhatsApp chat
2. Paste link: `https://captive.integralmass.com/`
3. **Expected Result**: Logo preview appears with title and description

### Method 3: Facebook Messenger
1. Open Messenger
2. Paste link in chat
3. **Expected Result**: Logo preview card appears

---

## Testing on Social Media

### Facebook
1. Create new post
2. Paste link: `https://captive.integralmass.com/`
3. **Expected Result**: Large preview card with logo, title, description

**Debug Tool**: https://developers.facebook.com/tools/debug/
- Paste your URL
- Click "Scrape Again" to refresh cache
- View preview

### LinkedIn
1. Create new post
2. Paste link: `https://captive.integralmass.com/`
3. **Expected Result**: Preview card with logo

**Debug Tool**: https://www.linkedin.com/post-inspector/
- Paste your URL
- View preview

### Twitter/X
1. Create new tweet
2. Paste link: `https://captive.integralmass.com/`
3. **Expected Result**: Large image card with logo

**Debug Tool**: https://cards-dev.twitter.com/validator
- Paste your URL
- Click "Preview card"

---

## What Each Page Shows

### Home Page (index.html)
- **Title**: "Integral Mass Captive Insurance"
- **Description**: "Actuarially sound captive insurance for prefab housing installation. Serving 12 General Contractors across three distinct market segments with <1% probability of ruin."
- **Logo**: captive-iMASS-logo.png

### Markets Page (markets.html)
- **Title**: "Market Segments | Integral Mass Captive Insurance"
- **Description**: "Three distinct market segments: Student Housing, Multi-Generational Living, and Rural Development. Uncorrelated risk profiles provide true diversification."
- **Logo**: captive-iMASS-logo.png

### Simulation Page (simulation.html)
- **Title**: "Simulation Results | Integral Mass Captive Insurance"
- **Description**: "Monte Carlo analysis with 5,000 simulations demonstrates <1% probability of ruin over 10 years."
- **Logo**: captive-iMASS-logo.png

### Compliance Page (compliance.html)
- **Title**: "Regulatory Compliance | Integral Mass Captive Insurance"
- **Description**: "Full compliance with Arizona Revised Statutes Title 20, Chapter 5, Article 2. Risk distribution across 12 independent GCs, $1M capitalization (4x minimum)."
- **Logo**: captive-iMASS-logo.png

---

## Troubleshooting

### Logo Not Appearing?

**Problem**: Logo doesn't show in preview
**Solutions**:
1. **Clear Cache**: Social platforms cache previews for 24-48 hours
2. **Use Debug Tools**: Force refresh using platform-specific debug tools
3. **Check URL**: Ensure using full domain (not localhost)
4. **Wait**: Sometimes takes a few minutes for platforms to fetch

### Facebook Specific:
- Use Facebook Debugger: https://developers.facebook.com/tools/debug/
- Click "Scrape Again" button
- This forces Facebook to re-fetch the page

### Twitter Specific:
- Use Twitter Card Validator: https://cards-dev.twitter.com/validator
- Preview updates immediately

### LinkedIn Specific:
- Use Post Inspector: https://www.linkedin.com/post-inspector/
- Clear cache if needed

---

## Browser Tab Icon (Favicon)

**Test**: Open any page in browser
**Expected**: Logo appears in browser tab next to page title

**Browsers to Test**:
- ✅ Chrome
- ✅ Safari
- ✅ Firefox
- ✅ Edge

---

## Technical Details

### Open Graph Tags (What Social Platforms Read)
```html
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Page Description">
<meta property="og:image" content="https://captive.integralmass.com/assets/captive-iMASS-logo.png">
<meta property="og:url" content="https://captive.integralmass.com/">
<meta property="og:type" content="website">
```

### Twitter Card Tags (What Twitter Reads)
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Page Description">
<meta name="twitter:image" content="https://captive.integralmass.com/assets/captive-iMASS-logo.png">
```

### Favicon (What Browsers Read)
```html
<link rel="icon" type="image/png" href="assets/captive-iMASS-logo.png">
```

---

## Image Requirements

### Current Logo:
- **File**: captive-iMASS-logo.png
- **Size**: 1.9MB
- **Location**: docs/assets/
- **Format**: PNG with transparency

### Optimal Social Media Image:
- **Recommended Size**: 1200x630px
- **Minimum Size**: 600x315px
- **Aspect Ratio**: 1.91:1
- **Format**: PNG or JPG
- **Max File Size**: 8MB (Facebook), 5MB (Twitter)

**Note**: Current logo (1.9MB) is within limits for all platforms.

---

## Quick Test Checklist

- [ ] Share link via SMS on iPhone - logo appears?
- [ ] Share link via WhatsApp - logo appears?
- [ ] Post link on Facebook - preview card shows logo?
- [ ] Post link on LinkedIn - preview card shows logo?
- [ ] Tweet link on Twitter - card shows logo?
- [ ] Open page in browser - favicon appears in tab?
- [ ] Check brand bar - Integral Mass link is sky blue?
- [ ] Check footer - social media icons present?

---

## Support Resources

### Debug Tools:
- **Facebook**: https://developers.facebook.com/tools/debug/
- **Twitter**: https://cards-dev.twitter.com/validator
- **LinkedIn**: https://www.linkedin.com/post-inspector/
- **Open Graph**: https://www.opengraph.xyz/

### Documentation:
- **Open Graph Protocol**: https://ogp.me/
- **Twitter Cards**: https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards
- **Facebook Sharing**: https://developers.facebook.com/docs/sharing/webmasters

---

## Success Criteria

✅ **Logo appears** when sharing link on phone (SMS, WhatsApp, Messenger)
✅ **Logo appears** when posting link on social media (Facebook, LinkedIn, Twitter)
✅ **Favicon appears** in browser tab
✅ **Brand bar** displays with sky blue Integral Mass link
✅ **Footer** displays with social media icons
✅ **All links** work correctly

---

**Status**: Ready for Testing

All meta tags, favicon, and branding elements are in place. Test on your phone and social media platforms to verify logo display.
