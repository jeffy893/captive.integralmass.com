# iPhone Link Preview Fix

## Issue
Logo was not appearing when sharing website links on iPhones via SMS/iMessage.

## Root Cause
iPhones require Apple Touch Icon tags in addition to standard favicon and Open Graph tags for link previews.

## Solution Implemented

### Added to All 4 HTML Pages:

```html
<!-- Favicon and Apple Touch Icons -->
<link rel="icon" type="image/png" href="assets/captive-iMASS-logo.png">
<link rel="apple-touch-icon" href="assets/captive-iMASS-logo.png">
<link rel="apple-touch-icon" sizes="152x152" href="assets/captive-iMASS-logo.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/captive-iMASS-logo.png">
<link rel="apple-touch-icon" sizes="167x167" href="assets/captive-iMASS-logo.png">
```

### Enhanced Open Graph Tags:

```html
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

## Apple Touch Icon Sizes Explained

- **Default** (no size): Used for older iOS devices
- **152x152**: iPad (non-Retina)
- **180x180**: iPhone (Retina)
- **167x167**: iPad Pro

## Testing on iPhone

### Method 1: iMessage/SMS
1. Open Messages app
2. Create new message
3. Paste: `https://captive.integralmass.com/`
4. **Expected**: Logo preview appears

### Method 2: Safari Share
1. Open link in Safari
2. Tap Share button
3. Select Messages or other app
4. **Expected**: Logo appears in preview

### Method 3: Add to Home Screen
1. Open link in Safari
2. Tap Share button
3. Select "Add to Home Screen"
4. **Expected**: Logo appears as app icon

## Cache Clearing

If logo still doesn't appear:

### On iPhone:
1. Settings → Safari → Clear History and Website Data
2. Restart Safari
3. Try sharing link again

### On Server:
- Apple caches link previews for 7 days
- May take time for new icons to propagate
- Use different URL parameters to force refresh: `?v=2`

## Files Updated

- ✅ `docs/index.html`
- ✅ `docs/markets.html`
- ✅ `docs/simulation.html`
- ✅ `docs/compliance.html`

## Commit Details

**Commit**: `223abe0`
**Message**: "Add Apple Touch Icons for iPhone link previews"
**Changes**: 4 files, 28 insertions, 4 deletions

## Additional Notes

### Why Multiple Sizes?
Different iOS devices and contexts use different icon sizes:
- Home screen icons
- Spotlight search
- Settings
- Link previews in Messages

### Image Requirements:
- **Format**: PNG (preferred) or JPG
- **Transparency**: Supported
- **Aspect Ratio**: Square (1:1)
- **Current File**: captive-iMASS-logo.png (1.9MB)

### Open Graph Image Requirements:
- **Minimum Size**: 600x315px
- **Recommended Size**: 1200x630px
- **Aspect Ratio**: 1.91:1
- **Max File Size**: 8MB (Facebook), 5MB (Twitter)

## Verification

### Check Meta Tags:
```bash
curl -s https://captive.integralmass.com/ | grep -i "apple-touch-icon"
```

### Debug Tools:
- **iMessage Link Preview**: Share link to yourself
- **Safari Web Inspector**: Check loaded resources
- **Facebook Debugger**: https://developers.facebook.com/tools/debug/

## Status

✅ **FIXED** - Apple Touch Icons added to all pages
✅ **PUSHED** - Changes deployed to GitHub
⏳ **TESTING** - May take time for Apple's cache to update

## Expected Timeline

- **Immediate**: New visitors see logo
- **1-7 days**: Cached previews update
- **Force Update**: Clear Safari cache or use URL parameter

---

**Date**: January 25, 2026
**Issue**: iPhone link preview missing logo
**Resolution**: Added Apple Touch Icon tags
**Status**: Deployed
