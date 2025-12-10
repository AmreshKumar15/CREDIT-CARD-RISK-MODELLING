# 🚀 Streamlit Cloud Deployment Guide for Lauki Finance

## Quick Deployment (3 Steps)

### Step 1: Prepare Your Repository

Ensure your GitHub repository has these files:
- ✅ `main.py` - Main Streamlit application
- ✅ `prediction_helper.py` - ML model and prediction logic
- ✅ `requirements.txt` - All dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `README.md` - Documentation
- ✅ CSV data files (customers.csv, loans.csv, bureau_data.csv)

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**: https://streamlit.io/cloud

2. **Sign up or Log in**
   - Click "Sign up" or "Sign in" with your GitHub account
   - Grant Streamlit access to your GitHub repositories

3. **Create a New App**
   - Click "New app" button
   - Select the repository: `AmreshKumar15/CREDIT-CARD-RISK-MODELLING`
   - Branch: `main`
   - File path: `main.py`
   - Click "Deploy"

4. **Wait for Deployment**
   - Streamlit will build and deploy your app
   - This typically takes 2-3 minutes
   - You can watch the build logs in real-time

### Step 3: Access Your Live App

Once deployed, your app will be available at:
```
https://<your-username>-creditcardriskmodelingapp.streamlit.app
```

Share this URL with anyone to access your live application!

## Environment-Specific Configuration

### For Streamlit Cloud

No additional configuration needed - Streamlit Cloud automatically:
- Installs dependencies from `requirements.txt`
- Reads configuration from `.streamlit/config.toml`
- Sets appropriate environment variables

### Local Development

To test before deployment:
```bash
streamlit run main.py
```

Visit `http://localhost:8501` in your browser

## Troubleshooting Deployment

### App Crashes or Won't Load

1. **Check the logs**: Click "Manage app" → "Settings" → "View logs"
2. **Verify requirements.txt**: Ensure all imports in Python files are listed
3. **Test locally first**: Run `streamlit run main.py` on your machine

### Slow Performance

1. **Optimize data loading**: Add caching decorators
2. **Use lighter visualizations**: Plotly is already optimized
3. **Reduce CSV file sizes**: Consider compressing data

### Memory Issues

Streamlit Cloud has 1GB of memory. If you hit this limit:
1. Load data more efficiently
2. Clear session state periodically
3. Use @st.cache_data decorators

## Advanced Features

### Add a Custom Domain

1. Go to your app settings on Streamlit Cloud
2. Add a custom domain (requires domain ownership)
3. Update DNS records to point to Streamlit

### Set Environment Variables

Create `.streamlit/secrets.toml`:
```toml
database_url = "postgresql://user:password@host/db"
api_key = "your_secret_key"
```

Access in code:
```python
import streamlit as st
api_key = st.secrets["api_key"]
```

### Link to GitHub for Auto-Updates

Your app automatically redeploys when you push to GitHub!
- No manual deployment needed
- New commits trigger automatic redeployment
- View deployment history in Streamlit Cloud dashboard

## Performance Optimization Tips

1. **Cache expensive operations**:
```python
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')
```

2. **Use session state for forms**:
```python
if 'age' not in st.session_state:
    st.session_state.age = 25
```

3. **Optimize visualizations**:
- Use Plotly (already optimized)
- Limit data points in charts
- Use downsampling for large datasets

## Monitoring Your Live App

1. **View traffic and usage**: Streamlit Cloud dashboard
2. **Monitor resource usage**: Check app logs
3. **Set up alerts**: Enable email notifications for crashes

## Sharing Your App

### Share URL
- Direct link: `https://<your-username>-creditcardriskmodelingapp.streamlit.app`
- Share with stakeholders, clients, and team members

### Embed in Website
```html
<iframe src="https://<your-username>-creditcardriskmodelingapp.streamlit.app?embedded=true" 
        width="100%" height="600" style="border: none;"></iframe>
```

### Social Media
Share with: #StreamlitCloud #DataScience #MachineLearning

## Best Practices

1. **Keep dependencies minimal**: Only include what you use
2. **Use .gitignore**: Don't commit sensitive data or large files
3. **Document your app**: Use docstrings and comments
4. **Version your dependencies**: Pin specific versions in requirements.txt
5. **Test thoroughly**: Run locally before deploying
6. **Monitor performance**: Check app logs regularly

## Security Considerations

1. **Never commit secrets**: Use `.streamlit/secrets.toml`
2. **Validate user input**: Sanitize all inputs
3. **Use HTTPS only**: Streamlit Cloud provides SSL/TLS
4. **Limit data exposure**: Don't log or display sensitive info
5. **Regular updates**: Keep dependencies updated

## FAQ

**Q: Can I deploy to other platforms?**
A: Yes! Heroku, AWS, Google Cloud, and others. See official Streamlit docs.

**Q: How do I update my deployed app?**
A: Just push to GitHub. Auto-redeploy happens automatically!

**Q: Can I use a custom domain?**
A: Yes, upgrade to Streamlit Cloud Professional tier.

**Q: Is there a free tier?**
A: Yes! Streamlit Cloud offers free deployment with resource limits.

**Q: How long does deployment take?**
A: Usually 2-3 minutes for first deployment, ~1-2 minutes for updates.

---

**Need Help?**
- Streamlit Docs: https://docs.streamlit.io
- Community Forum: https://discuss.streamlit.io
- GitHub Issues: https://github.com/streamlit/streamlit/issues

**Happy Deploying! 🚀**
