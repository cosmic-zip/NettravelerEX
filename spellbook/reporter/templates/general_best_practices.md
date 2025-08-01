# **General Best Practices**


### **Authentication and Credential Hygiene**

- **Strong Passwords:** Use complex combinations (minimum 12 characters, with letters, numbers, and symbols).  
- **Enforce password complexity and lockout thresholds.**  
- **Stop reusing passwords and don't leave default passwords anywhere.**  
- **Set long, complex passwords for SPN accounts.**  
- **Use LAPS for managing local admin passwords.**  
- **Don't hardcode credentials in your code, scripts, binaries.**  
- **Multi-Factor Authentication (MFA/2FA):**  
    - **2FA (Two-Factor):** Requires a second authentication method (e.g., SMS, Google Authenticator).  
    - **MFA (Multi-Factor):** May include biometrics, hardware tokens, or additional layers beyond 2FA.  


### **Access Control and Privilege Management**

- **Verify the permissions on the shares and on the local drives, especially where high privileged software resides.**  
- **Search your network shares for "password" — you’ll be amazed (and terrified).**  
- **Have a look at how many users are in the domain admin group. Do they actually need to be that many?**  
- **Implement App Control or AppLocker.**  


### **Network and Protocol Hardening**

- **Enable SMB signing.**  
- **Disable WPAD, LLMNR, and other Microsoft multicast name resolution "features."**  
- **Close unnecessary ports on the firewall, and monitor whatever you do allow to go through, for example with a TLS terminating web proxy.**  


### **System Maintenance and Monitoring**

- **Regular Updates:** Keep systems, plugins, and dependencies up to date.  
- **Patch**  
- **Automated Protection:**  
    - Antivirus (for endpoints)  
    - Firewall (to filter malicious traffic)  
    - IDS/IPS (intrusion detection/prevention systems)  


### **Certificate and Protocol Use**

- **Don't ignore certificate errors, this is one of the most innocent looking findings in vulnerability scans but can cause so much trouble. Or maybe you are not having certificate errors because you just choose plaintext protocols?**  

