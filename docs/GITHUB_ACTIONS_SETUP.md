# GitHub Actions Automation Setup

Set up weekly automatic data updates for your timetable kiosk using GitHub Actions.

## 🎯 What This Does

GitHub Actions will automatically:

- Fetch fresh data from your Sentral API every Monday at 5:00 AM
- Update the kiosk with current timetables for the week
- Maintain up-to-date information without manual intervention

## ⚡ Quick Setup

### Step 1: Repository Secrets

1. **Go to your repository** on GitHub
2. **Navigate to**: Settings → Secrets and variables → Actions
3. **Add these secrets**:
   - `REST_API_KEY`: Your Sentral REST API key
   - `LISS_PASSWORD`: Your LISS system password (if used)

### Step 2: Enable Workflows

1. **Go to Actions tab** in your repository
2. **Enable workflows** if prompted
3. **Workflows are now active** and will run weekly

### Step 3: Manual Data Update

1. **Go to Actions tab**
2. **Select "Weekly Data Update"** workflow
3. **Click "Run workflow"** → Run workflow
4. **Wait for completion** (usually 1-2 minutes)
5. **Your kiosk now has fresh data**

## 🔧 Configuration

### Getting Your API Key

1. **Login to Sentral**: `https://<your-school-sentral>/`
2. **Navigate to**: Admin → Integrations → REST API → Configure
3. **Generate API key** if you don't have one
4. **Copy the key** for use in repository secrets

### Repository Secrets Setup

**REST_API_KEY**:

- Value: Your Sentral API key (e.g., `abc123def456ghi789`)
- Used by: All data generation workflows

**LISS_PASSWORD** (optional):

- Value: Your LISS system password
- Used by: LISS-specific data generation only

### Workflow Files

The following workflows are included:

- **Weekly Data Update**: Updates bell times and calendar data weekly
- **Generate LISS Info**: Updates timetable data (`generate_liss_info.py`)

## 📅 Automation Schedule

By default, workflows run:

- **Weekly**: Every Monday at 5:00 AM Sydney time (automatic)
- **Manually**: Click "Run workflow" anytime
- **On push**: When code is updated

### Current Schedule

The main data update runs weekly:

```yaml
on:
  schedule:
    - cron: "0 19 * * 0" # 5:00 AM Monday Sydney (AEST)
    - cron: "0 18 * * 0" # 5:00 AM Monday Sydney (AEDT)
  workflow_dispatch: # Manual trigger
```

## 🔍 Monitoring

### Check Workflow Status

1. **Go to Actions tab**
2. **View recent runs** and their status
3. **Click on a run** to see detailed logs
4. **Green checkmark** = success, **Red X** = failure

### Troubleshooting Failed Runs

**Common Issues**:

- **API key invalid**: Check REST_API_KEY secret
- **Network timeout**: Retry the workflow
- **Data format error**: Check Sentral API availability

**View Error Details**:

1. Click on failed workflow run
2. Expand the failed step
3. Read error messages in logs
4. Fix issues and re-run workflow

### Git Conflict Issues (Fixed in v2.1)

If you see errors like:

```
error: Your local changes to the following files would be overwritten by merge:
    .logs/liss_info_generation.log
    liss_info.json
Please commit your changes or stash them before you merge.
```

**This has been resolved** in version 2.1 of the workflows. The actions now automatically:

- Stash local changes before pulling updates
- Apply the latest changes from remote
- Restore the generated files
- Commit and push successfully

If you're still experiencing this issue, ensure your workflows are up to date.

## ⚙️ Advanced Configuration

### Custom Data Update Scripts

To modify what data is fetched:

1. Edit the Python scripts (`generate_*.py`)
2. Update `config.json` API settings for new endpoints
3. Commit changes to trigger updated workflows

### Multiple School Support

For managing multiple schools:

1. Create separate repositories for each school
2. Use different API keys in each repository's secrets
3. Customize `config.json` for each school's branding

### Environment Variables

All workflows use these environment variables:

- `REST_API_KEY`: From repository secrets
- `LISS_PASSWORD`: From repository secrets (optional)
- GitHub provides: `GITHUB_TOKEN`, `GITHUB_WORKSPACE`, etc.

## 🚀 Benefits

**Automated Updates**:

- Fresh data every Monday morning without manual intervention
- Consistent, reliable weekly updates
- Optimal timing for school week preparation
- No need to remember to update manually

**Version Control**:

- All changes tracked in Git history
- Easy to revert if something goes wrong
- Collaborative editing with team members

**Free Hosting**:

- GitHub Actions included with free GitHub accounts
- GitHub Pages hosting also free
- No additional server costs

## 🆘 Support

**Workflows not running?**

- Check repository secrets are set correctly
- Ensure workflows are enabled in Actions tab
- Verify your API key has necessary permissions

**Data not updating?**

- Check workflow run logs for errors
- Test API key manually with Sentral
- Ensure your school's API endpoints are accessible

**Need help?**

- Review workflow logs in Actions tab
- Check [Debugging Guide](DEBUGGING_GUIDE.md) for troubleshooting
- Verify [Configuration Guide](CONFIGURATION.md) settings
