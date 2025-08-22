# GitHub Actions Setup for LISS Bell Times

This GitHub Action automatically fetches bell times from the LISS API every day at 6:00 AM Sydney time.

## 🚀 Quick Setup

### 1. Set up GitHub Secrets

The workflow requires LISS credentials to be stored as GitHub repository secrets:

1. **Go to your GitHub repository**
2. **Navigate to Settings → Secrets and variables → Actions**
3. **Click "New repository secret"**
4. **Add these secrets:**

   ```
   Name: LISS_USERNAME
   Value: your_username

   Name: LISS_PASSWORD
   Value: your_password
   ```

### 2. Enable GitHub Actions

1. **Go to the Actions tab** in your repository
2. **Enable workflows** if prompted
3. **The workflow will appear** as "Update Bell Times from LISS"

### 3. Test the Setup

You can manually trigger the workflow to test it:

1. **Go to Actions → Update Bell Times from LISS**
2. **Click "Run workflow"**
3. **Select "Run connection test only"** for initial testing
4. **Click "Run workflow"**

## ⏰ Schedule Details

The workflow runs **twice daily** to account for Sydney's daylight saving time:

- **8:00 PM UTC** (6:00 AM AEST - Standard Time)
- **7:00 PM UTC** (6:00 AM AEDT - Daylight Saving Time)

This ensures it runs at 6:00 AM Sydney time year-round.

## 🔧 Workflow Features

### Automatic Execution

- ✅ Fetches bell times from LISS API
- ✅ Saves to `current_bell_times.json`
- ✅ Commits changes to repository
- ✅ Creates workflow summary

### Manual Execution

- 🧪 Test connection only mode
- 🔄 Full bell times update
- 📊 Detailed logging and summaries

### Error Handling

- ❌ Graceful failure handling
- 📝 Detailed error messages
- 🚨 Clear troubleshooting guidance

### Security

- 🔒 Credentials stored as GitHub secrets
- 🛡️ No sensitive data in logs
- 🔐 Secure environment variable handling

## 📁 Generated Files

The workflow creates/updates:

- **`current_bell_times.json`** - Current bell times data
- **Workflow artifacts** - Historical bell times (30-day retention)
- **Commit history** - Automatic commits when data changes

## 🐞 Troubleshooting

### Common Issues

**❌ Workflow fails with "LISS credentials not set"**

- Check that `LISS_USERNAME` and `LISS_PASSWORD` secrets are properly configured
- Verify secret names match exactly (case-sensitive)

**❌ Connection test passes but no bell times fetched**

- This is likely the academic year restriction we've seen before
- Contact school IT about 2025 academic year data availability

**❌ Workflow doesn't run at expected time**

- GitHub Actions may have delays during peak times
- Check the "Next run" time in the Actions tab

**❌ No files committed**

- The workflow only commits when bell times data actually changes
- Check workflow logs for "No changes detected" messages

### Viewing Logs

1. **Go to Actions tab**
2. **Click on a workflow run**
3. **Click on "update-bell-times" job**
4. **Expand each step** to see detailed logs

### Manual Testing

Test the workflow locally:

```bash
# Set environment variables
export LISS_USERNAME=your_username
export LISS_PASSWORD=your_password

# Test connection
python3 liss_bell_times.py --test-only

# Fetch bell times
python3 liss_bell_times.py
```

## 🔄 Customization

### Change Schedule

Edit `.github/workflows/update-bell-times.yml`:

```yaml
schedule:
  - cron: "0 20 * * *" # Change time here (UTC)
```

Use [crontab.guru](https://crontab.guru/) to help with cron syntax.

### Change Output File

Edit `liss_config.json`:

```json
{
  "output": {
    "file": "your_custom_filename.json"
  }
}
```

### Add Notifications

Add notification steps to the workflow:

```yaml
- name: Send notification
  if: failure()
  # Add your notification service here
  # (Slack, Teams, email, etc.)
```

## 📊 Monitoring

The workflow provides:

- **Step summaries** with execution details
- **Artifact uploads** for historical data
- **Commit messages** showing update timestamps
- **Failure notifications** with troubleshooting tips

## 🔐 Security Best Practices

- ✅ Credentials stored as GitHub secrets
- ✅ No secrets in workflow files
- ✅ Environment variables used throughout
- ✅ Minimal permissions model
- ✅ Secure artifact handling

## 🆘 Support

If you encounter issues:

1. **Check workflow logs** for detailed error messages
2. **Test locally** with the same credentials
3. **Verify secrets** are correctly configured
4. **Contact school IT** for LISS system issues
5. **Check LISS documentation** for API changes

The workflow is designed to be robust and provide clear feedback about any issues that occur.
