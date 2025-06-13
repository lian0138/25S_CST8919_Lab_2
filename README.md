## Lab Summary

In this lab, I deployed a Python Flask app with a `/login` endpoint to Azure Web App. I enabled logging via Log Analytics and set up an alert to detect failed login attempts.

## Challenges

- Ensuring that diagnostic settings correctly deliver logs.

## Improvements

For real-world scenarios, if a user logs in fails 5 times in 5 minutes, I will block their IP address in the firewall. In the traditional Linux environment, I can use fail2ban to put that IP address into the banning pool of iptables periodically.

## KQL Query

```
AppServiceConsoleLogs
| where ResultDescription contains "Fail"
| order by TimeGenerated desc
```

*Explanation:*
- Filters logs for entries where the ResultDescription includes "Fail".
- Orders the results by the time generated in descending order.

## Youtube link
https://www.youtube.com/watch?v=kyZa0TI1Xz8