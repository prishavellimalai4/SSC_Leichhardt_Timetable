# GitHub Pages Deployment Guide

This guide provides step-by-step instructions for deploying the School Timetable Kiosk to GitHub Pages.

## Why GitHub Pages?

✅ **Free hosting** for public repositories  
✅ **Automatic HTTPS** with custom domain support  
✅ **Global CDN** for fast worldwide access  
✅ **No CORS issues** - serves files properly  
✅ **Easy updates** via Git commits  
✅ **Perfect for school kiosks** and public displays  

## Step-by-Step Deployment

### 1. Prepare Your Repository

**Option A: Fork this repository**
1. Click "Fork" on the main repository page
2. Clone your fork: `git clone https://github.com/yourusername/your-repo-name.git`

**Option B: Create new repository**
1. Create a new repository on GitHub
2. Clone it locally: `git clone https://github.com/yourusername/your-repo-name.git`
3. Copy the required files into the repository folder

### 2. Required Files

Ensure these files are in your repository root:
```
├── index.html
├── config.json
├── bell_times.xml
├── liss_info.xml
├── calendar.xml
└── docs/
    ├── README.md (optional)
    ├── CONFIGURATION.md (optional)
    └── GITHUB_PAGES_DEPLOYMENT.md (optional)
```

### 3. Customize Configuration

1. **Edit `config.json`** with your school's details:
   - School name and logo URL
   - Colors and styling
   - Period configurations
   - Sport period settings
   - Year group settings

2. **Update XML files** with your school's data:
   - `bell_times.xml` - Your bell schedule
   - `liss_info.xml` - Your lesson data
   - `calendar.xml` - Your calendar with day types

### 4. Enable GitHub Pages

1. **Go to your repository** on GitHub.com
2. **Click Settings** tab
3. **Scroll down to "Pages"** in the left sidebar
4. **Under "Source"**, select:
   - **Source**: Deploy from a branch
   - **Branch**: main (or master)
   - **Folder**: / (root)
5. **Click "Save"**

### 5. Access Your Timetable

- **Your URL will be**: `https://yourusername.github.io/repository-name`
- **Initial deployment** takes 1-10 minutes
- **Check deployment status** in the Actions tab

## Custom Domain (Optional)

### Using a School Domain

1. **Add a CNAME file** to your repository root:
   ```
   timetable.yourschool.edu.au
   ```

2. **Configure DNS** at your domain provider:
   - Add CNAME record: `timetable` → `yourusername.github.io`

3. **Update GitHub Pages settings**:
   - Go to Settings → Pages
   - Enter your custom domain: `timetable.yourschool.edu.au`
   - Enable "Enforce HTTPS"

## Updating Your Timetable

### Making Changes

1. **Edit files locally** or directly on GitHub
2. **Commit changes**:
   ```bash
   git add .
   git commit -m "Update timetable configuration"
   git push
   ```
3. **Changes appear** within 1-5 minutes

### Common Updates

- **New semester**: Update `liss_info.xml` with new classes
- **Schedule changes**: Modify `bell_times.xml`
- **Calendar updates**: Update `calendar.xml` with new dates
- **Styling changes**: Modify colors in `config.json`

## Security Considerations

⚠️ **Public Repository**: All files are publicly visible  
⚠️ **No sensitive data**: Don't include private information  
⚠️ **Student privacy**: Ensure compliance with privacy policies  

### Best Practices

- Use generic class codes rather than student names
- Consider abbreviating teacher names if privacy is a concern
- Regularly review what data is publicly accessible
- Use private repositories if handling sensitive data (requires GitHub Pro)

## Troubleshooting

### Common Issues

**404 Error when accessing site:**
- Check repository name matches URL
- Ensure GitHub Pages is enabled
- Verify files are in root directory (not in subfolder)

**Site shows old data:**
- Clear browser cache (Ctrl+F5)
- Check if changes were committed and pushed
- Verify GitHub Pages deployment completed (Actions tab)

**Configuration not loading:**
- Check `config.json` syntax (use JSON validator)
- Ensure file is named exactly `config.json`
- Check browser console for error messages (F12)

**XML files not loading:**
- Verify file names match configuration
- Check XML syntax is valid
- Ensure files are in same directory as `index.html`

### Getting Help

- Check browser console (F12) for error messages
- Review GitHub Pages documentation
- Verify all files are committed and pushed
- Test configuration locally first

## Performance Tips

✅ **Optimize images**: Compress logo files  
✅ **Minimize XML**: Remove unnecessary whitespace  
✅ **Use CDN**: GitHub Pages provides global CDN  
✅ **Enable caching**: Configure refresh intervals appropriately  
✅ **Monitor usage**: Check repository insights for traffic  

## Example URLs

- **Tempe HS Example**: `https://tempehs.github.io/Tempe_HS_Timetable_Kiosk`
- **Your School**: `https://yourschool.github.io/school-timetable`
- **With Custom Domain**: `https://timetable.yourschool.edu.au`

This setup provides a professional, reliable, and free hosting solution perfect for school timetable displays!
