def check_alerts(df):
    active_alerts = []
    if df.empty:
        return active_alerts

    if len(df) > 50:
        active_alerts.append("🆘 High Traffic Volume!")
    if (df['fare'] > 100000).any():
        active_alerts.append("🚨 High Fare Detected!")
        
    return active_alerts
