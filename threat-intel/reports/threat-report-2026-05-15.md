# Threat Intelligence Report — May 15, 2026

> **Generated:** 2026-05-15 04:26 UTC  
> **Total items collected:** 44  
> **Sources:** 5

---

## Summary

- **HIGH**: 11 item(s)
- **UNKNOWN**: 33 item(s)

---

## CISA Known Exploited Vulnerabilities

### CVE-2026-20182 – Cisco Catalyst SD-WAN Controller Authentication Bypass Vulnerability

**Severity:** `HIGH`  
**Vendor:** Cisco — **Product:** Catalyst SD-WAN  
**Published:** 2026-05-14  

Cisco Catalyst SD-WAN Controller & Manager contain an authentication bypass vulnerability that allows an unauthenticated, remote attacker to bypass authentication and obtain administrative privileges on an affected system.

> **Required Action:** Please adhere to CISA’s guidelines to assess exposure and mitigate risks associated with Cisco SD-WAN devices as outlined in CISA’s Emergency Directive 26-03 (URL listed below in Notes) and CISA’s Hunt & Hardening Guidance for Cisco SD-WAN Devices (URL listed below in Notes). Adhere to the applicable BOD 22-01 guidance for cloud services or discontinue use of the product if mitigations are not available.

---

### CVE-2026-42208 – BerriAI LiteLLM SQL Injection Vulnerability

**Severity:** `HIGH`  
**Vendor:** BerriAI — **Product:** LiteLLM  
**Published:** 2026-05-08  

BerriAI LiteLLM contains a SQL injection vulnerability that allows an attacker to read data from the proxy's database and potentially modify it, leading to unauthorized access to the proxy and the credentials it manages.

> **Required Action:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

---

### CVE-2026-6973 – Ivanti Endpoint Manager Mobile (EPMM) Improper Input Validation Vulnerability

**Severity:** `HIGH`  
**Vendor:** Ivanti — **Product:** Endpoint Manager Mobile (EPMM)  
**Published:** 2026-05-07  

Ivanti Endpoint Manager Mobile (EPMM) contains an improper input validation vulnerability that allows a remotely authenticated user with administrative access to achieve remote code execution.

> **Required Action:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

---

### CVE-2026-0300 – Palo Alto Networks PAN-OS Out-of-bounds Write Vulnerability

**Severity:** `HIGH`  
**Vendor:** Palo Alto Networks — **Product:** PAN-OS  
**Published:** 2026-05-06  

Palo Alto Networks PAN-OS contains an out-of-bounds write vulnerability in the User-ID Authentication Portal (aka Captive Portal) service that can allow an unauthenticated attacker to execute arbitrary code with root privileges on the PA-Series and VM-Series firewalls by sending specially crafted packets.

> **Required Action:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable. Until the vendor releases an official fix, the following workaround should be implemented:  - Restrict User-ID Authentication Portal access to only trusted zones.  - Disable User-ID Authentication Portal if not required. 5/13/2026: Palo Alto has released a variety of patches. If these are relevant to your environment, please apply the designated patch.

---

### CVE-2026-31431 – Linux Kernel Incorrect Resource Transfer Between Spheres Vulnerability

**Severity:** `HIGH`  
**Vendor:** Linux — **Product:** Kernel  
**Published:** 2026-05-01  

Linux Kernel contains an incorrect resource transfer between spheres vulnerability that could allow for privilege escalation.

> **Required Action:** "Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

---

### CVE-2026-41940 – WebPros cPanel & WHM and WP2 (WordPress Squared) Missing Authentication for Critical Function Vulnerability

**Severity:** `HIGH`  
**Vendor:** WebPros — **Product:** cPanel & WHM and WP2 (WordPress Squared)  
**Published:** 2026-04-30  

WebPros cPanel & WHM (WebHost Manager) and WP2 (WordPress Squared) contain an authentication bypass vulnerability in the login flow that allows unauthenticated remote attackers to gain unauthorized access to the control panel.

> **Required Action:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

---

### CVE-2024-1708 – ConnectWise ScreenConnect Path Traversal Vulnerability

**Severity:** `HIGH`  
**Vendor:** ConnectWise — **Product:** ScreenConnect  
**Published:** 2026-04-28  

ConnectWise ScreenConnect contains a path traversal vulnerability which could allow an attacker to execute remote code or directly impact confidential data and critical systems.

> **Required Action:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

---

### CVE-2026-32202 – Microsoft Windows Protection Mechanism Failure Vulnerability

**Severity:** `HIGH`  
**Vendor:** Microsoft — **Product:** Windows  
**Published:** 2026-04-28  

Microsoft Windows Shell contains a protection mechanism failure vulnerability that allows an unauthorized attacker to perform spoofing over a network.

> **Required Action:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

---

### CVE-2025-29635 – D-Link DIR-823X Command Injection Vulnerability

**Severity:** `HIGH`  
**Vendor:** D-Link — **Product:** DIR-823X  
**Published:** 2026-04-24  

D-Link DIR-823X contains a command injection vulnerability that allows an authorized attacker to execute arbitrary commands on remote devices by sending a POST request to /goform/set_prohibiting via the corresponding function. The impacted product could be end-of-life (EoL) and/or end-of-service (EoS). Users should discontinue product utilization.

> **Required Action:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

---

### CVE-2024-7399 – Samsung MagicINFO 9 Server Path Traversal Vulnerability

**Severity:** `HIGH`  
**Vendor:** Samsung — **Product:** MagicINFO 9 Server  
**Published:** 2026-04-24  

Samsung MagicINFO 9 Server contains a path traversal vulnerability that could allow an attacker to write arbitrary files as system authority.

> **Required Action:** Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

---

## NIST NVD Recent CVEs

### CVE-1999-0095 (CVSS 10.0)

**CVSS Score:** 10.0  
**Published:** 1988-10-01T04:00:00.000  

The debug command in Sendmail is enabled, allowing attackers to execute commands as root.

---

### CVE-1999-0082 (CVSS 10.0)

**CVSS Score:** 10.0  
**Published:** 1988-11-11T05:00:00.000  

CWD ~root command in ftpd allows root access.

---

### CVE-1999-1471 (CVSS 7.2)

**CVSS Score:** 7.2  
**Published:** 1989-01-01T05:00:00.000  

Buffer overflow in passwd in BSD based operating systems 4.3 and earlier allows local users to gain root privileges by specifying a long shell or GECOS field.

---

### CVE-1999-1122 (CVSS 4.6)

**CVSS Score:** 4.6  
**Published:** 1989-07-26T04:00:00.000  

Vulnerability in restore in SunOS 4.0.3 and earlier allows local users to gain privileges.

---

### CVE-1999-1467 (CVSS 10.0)

**CVSS Score:** 10.0  
**Published:** 1989-10-26T04:00:00.000  

Vulnerability in rcp on SunOS 4.0.x allows remote attackers from trusted hosts to execute arbitrary commands as root, possibly related to the configuration of the nobody user.

---

### CVE-1999-1506 (CVSS 7.5)

**CVSS Score:** 7.5  
**Published:** 1990-01-29T05:00:00.000  

Vulnerability in SMI Sendmail 4.0 and earlier, on SunOS up to 4.0.3, allows remote attackers to access user bin.

---

### CVE-1999-0084 (CVSS 8.4)

**Severity:** `HIGH`  
**CVSS Score:** 8.4  
**Published:** 1990-05-01T04:00:00.000  

Certain NFS servers allow users to use mknod to gain privileges by creating a writable kmem device and setting the UID to 0.

---

### CVE-2000-0388 (CVSS 7.5)

**CVSS Score:** 7.5  
**Published:** 1990-05-09T04:00:00.000  

Buffer overflow in FreeBSD libmytinfo library allows local users to execute commands via a long TERMCAP environmental variable.

---

### CVE-1999-0209 (CVSS 5.0)

**CVSS Score:** 5.0  
**Published:** 1990-08-14T04:00:00.000  

The SunView (SunTools) selection_svc facility allows remote users to read files.

---

### CVE-1999-1198 (CVSS 7.2)

**CVSS Score:** 7.2  
**Published:** 1990-10-03T04:00:00.000  

BuildDisk program on NeXT systems before 2.0 does not prompt users for the root password, which allows local users to gain root privileges.

---

## US-CERT Alerts

### Siemens Siemens ROS#

**Published:** Thu, 14 May 26 12:00:00 +0000  

View CSAF
Summary
ROS# contains a ROS service file_server, that before version 2.2.2 contains a path traversal vulnerability which could allow an attacker to access, i.e. read and write, arbitrary files, which are accessible with the user rights of the user that runs the service, on the system that hosts service. Siemens has released a new version for ROS# and recommends to update to the latest ve

[Read more →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-08)

---

### Siemens gWAP

**Published:** Thu, 14 May 26 12:00:00 +0000  

View CSAF
Summary
Siemens gPROMS Web Applications Publisher (gWAP) is affected by a remote code execution vulnerability introduced through a third-party component, namely the Axios HTTP client library. The vulnerability stems from a specific "Gadget" attack chain that allows prototype pollution in other third-party libraries, potentially allowing an attacker to execute arbitrary code. Siemens has 

[Read more →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-01)

---

### Siemens SIMATIC

**Published:** Thu, 14 May 26 12:00:00 +0000  

View CSAF
Summary
SIMATIC CN 4100 contains multiple vulnerabilities which could potentially lead to a compromise in availability, integrity and confidentiality. Siemens has released a new version for SIMATIC CN 4100 and recommends to update to the latest version.
The following versions of Siemens SIMATIC are affected:

SIMATIC CN 4100 vers:intdot/&lt;5.0&nbsp;





CVSS
Vendor
Equipment
Vulnerabil

[Read more →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-10)

---

### Siemens Ruggedcom Rox

**Published:** Thu, 14 May 26 12:00:00 +0000  

View CSAF
Summary
Ruggedcom Rox contains an input validation vulnerability in the Scheduler functionality that could allow an authenticated remote attacker to execute arbitrary commands with root privileges on the underlying operating system. Siemens has released new versions for the affected products and recommends to update to the latest versions.
The following versions of Siemens Ruggedcom Rox 

[Read more →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-12)

---

### Siemens Ruggedcom Rox

**Published:** Thu, 14 May 26 12:00:00 +0000  

View CSAF
Summary
Ruggedcom Rox before v2.17.1 contain multiple third-party vulnerabilities. Siemens has released new versions for the affected products and recommends to update to the latest versions.
The following versions of Siemens Ruggedcom Rox are affected:

RUGGEDCOM ROX MX5000 vers:intdot/&lt;2.17.1 (CVE-2019-13103, CVE-2019-13104, CVE-2019-13106, CVE-2019-14192, CVE-2019-14193, CVE-2019-1

[Read more →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-16)

---

### Siemens Simcenter Femap

**Published:** Thu, 14 May 26 12:00:00 +0000  

View CSAF
Summary
Simcenter Femap is affected by heap based buffer overflow vulnerability in Datakit library that could be triggered when the application reads files in IPT format. If a user is tricked to open a malicious file with the affected application, an attacker could leverage the vulnerability to perform remote code execution in the context of the current process. Siemens has released a ne

[Read more →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-05)

---

### Universal Robots Polyscope 5

**Published:** Thu, 14 May 26 12:00:00 +0000  

View CSAF
Summary
Successful exploitation of these vulnerabilities could allow an attacker to bypass authentication and execute code.
The following versions of Universal Robots Polyscope 5 are affected:

Polyscope 5 &lt;5.25.1&nbsp;





CVSS
Vendor
Equipment
Vulnerabilities




v3 9.8
Universal Robots
Universal Robots Polyscope 5
Improper Neutralization of Special Elements used in an OS Command (

[Read more →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-17)

---

### Siemens Ruggedcom Rox

**Published:** Thu, 14 May 26 12:00:00 +0000  

View CSAF
Summary
Ruggedcom Rox contains an input validation vulnerability in the feature key installation process that could allow an authenticated remote attacker to execute arbitrary commands with root privileges on the underlying operating system. Siemens has released new versions for the affected products and recommends to update to the latest versions.
The following versions of Siemens Rugge

[Read more →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-134-11)

---

## Bleeping Computer Security News

### TeamPCP hackers advertise Mistral AI code repos for sale

**Published:** Thu, 14 May 2026 18:50:36 -0400  

The TeamPCP hacker group is threatening to leak source code from the Mistral AI project unless a buyer is found for the data. [...]

[Read more →](https://www.bleepingcomputer.com/news/security/teampcp-hackers-advertise-mistral-ai-code-repos-for-sale/)

---

### Hackers exploit auth bypass flaw in Burst Statistics WordPress plugin

**Published:** Thu, 14 May 2026 17:07:17 -0400  

Hackers are leveraging a critical authentication bypass vulnerability in the WordPress plugin Burst Statistics to obtain admin-level access to websites. [...]

[Read more →](https://www.bleepingcomputer.com/news/security/hackers-exploit-auth-bypass-flaw-in-burst-statistics-wordpress-plugin/)

---

### Cisco warns of new critical SD-WAN flaw exploited in zero-day attacks

**Published:** Thu, 14 May 2026 16:09:56 -0400  

Cisco is warning that a critical Catalyst SD-WAN Controller authentication bypass flaw, tracked as CVE-2026-20182, was actively exploited in zero-day attacks that allowed attackers to gain administrative privileges on compromised devices. [...]

[Read more →](https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-critical-sd-wan-flaw-exploited-in-zero-day-attacks/)

---

### OpenAI confirms security breach in TanStack supply chain attack

**Published:** Thu, 14 May 2026 15:07:24 -0400  

OpenAI says two employees' devices were breached in the recent TanStack supply chain attack that impacted hundreds of npm and PyPI packages, causing the company to rotate code-signing certificates for its applications as a precaution. [...]

[Read more →](https://www.bleepingcomputer.com/news/security/openai-confirms-security-breach-in-tanstack-supply-chain-attack/)

---

### Windows 11 and Microsoft Edge hacked at Pwn2Own Berlin 2026

**Published:** Thu, 14 May 2026 14:53:50 -0400  

On the first day of Pwn2Own Berlin 2026, security researchers collected $523,000 in cash awards after exploiting 24 unique zero-days. [...]

[Read more →](https://www.bleepingcomputer.com/news/security/windows-11-and-microsoft-edge-hacked-on-first-day-of-pwn2own-berlin-2026/)

---

### 18-year-old NGINX vulnerability allows DoS, potential RCE

**Published:** Thu, 14 May 2026 11:43:41 -0400  

An 18-year-old flaw in the NGINX open-source web server, discovered using an autonomous scanning system, can be exploited for denial of service and, under certain conditions, remote code execution. [...]

[Read more →](https://www.bleepingcomputer.com/news/security/18-year-old-nginx-vulnerability-allows-dos-potential-rce/)

---

### Cyber-Enabled Cargo Crime: How Cybercrime Tradecraft is Used to Steal Freight

**Published:** Thu, 14 May 2026 11:21:32 -0400  

Cargo theft now starts with phishing emails and stolen credentials, not hijackings, to reroute and steal freight from supply chains. NMFTA outlines how cyber-enabled cargo crime is changing transportation security. [...]

[Read more →](https://www.bleepingcomputer.com/news/security/cyber-enabled-cargo-crime-how-cybercrime-tradecraft-is-used-to-steal-freight/)

---

### KongTuke hackers now use Microsoft Teams for corporate breaches

**Published:** Thu, 14 May 2026 08:12:40 -0400  

Initial access broker KongTuke has moved to Microsoft Teams for social engineering attacks, taking as little as five minutes to gain persistent access to corporate networks. [...]

[Read more →](https://www.bleepingcomputer.com/news/security/kongtuke-hackers-now-use-microsoft-teams-for-corporate-breaches/)

---

## The Hacker News

### Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Access

**Published:** Thu, 14 May 2026 23:15:20 +0530  

Cisco has released updates to address a maximum-severity authentication bypass flaw in Catalyst SD-WAN Controller that it said has been exploited in limited attacks.
The vulnerability, tracked as CVE-2026-20182, carries a CVSS score of 10.0.
"A vulnerability in the peering authentication in Cisco Catalyst SD-WAN Controller, formerly SD-WAN vSmart, and Cisco Catalyst SD-WAN Manager, formerly

[Read more →](https://thehackernews.com/2026/05/cisco-catalyst-sd-wan-controller-auth.html)

---

### Stealer Backdoor Found in 3 Node-IPC Versions Targeting Developer Secrets

**Published:** Thu, 14 May 2026 22:52:43 +0530  

Cybersecurity researchers are sounding the alarm about what has been described as "malicious activity" in newly published versions of node-ipc.
According to Socket and StepSecurity, three different versions of the npm package have been confirmed as malicious -

node-ipc@9.1.6
node-ipc@9.2.3
node-ipc@12.0.1

"Early analysis indicates that node-ipc@9.1.6, node-ipc@9.2.3, and node-ipc@12.0.1

[Read more →](https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html)

---

### ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks, and 10+ Stories

**Published:** Thu, 14 May 2026 21:37:46 +0530  

Everything is still on fire.
This week feels dumb in the worst way — bad links, weak checks, fake help desks, shady forum posts, and people turning supply chain attacks into some cursed little game for clout and cash. Half of it feels new. Half of it feels like crap we should have fixed years ago.
The mess keeps getting louder: users get tricked, boxes get popped, tools meant for normal work

[Read more →](https://thehackernews.com/2026/05/threatsday-bulletin-pan-os-rce-mythos.html)

---

### Ghostwriter Targets Ukrainian Government With Geofenced PDF Phishing, Cobalt Strike

**Published:** Thu, 14 May 2026 19:30:37 +0530  

The Belarus-aligned threat group known as Ghostwriter has been attributed to a fresh set of attacks targeting governmental organizations in Ukraine.
Active since at least 2016, Ghostwriter has been linked to both cyber espionage and influence operations targeting neighboring countries, particularly Ukraine. It's also tracked under the monikers FrostyNeighbor, PUSHCHA, Storm-0257, TA445, UAC‑0057

[Read more →](https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html)

---

### PraisonAI CVE-2026-44338 Auth Bypass Targeted Within Hours of Disclosure

**Published:** Thu, 14 May 2026 17:10:14 +0530  

Threat actors have been observed attempting to exploit a recently disclosed security vulnerability in PraisonAI, an open-source multi-agent orchestration framework, within four hours of public disclosure.
The vulnerability in question is CVE-2026-44338 (CVSS score: 7.3), a case of missing authentication that exposes sensitive endpoints to anyone, potentially allowing an attacker to invoke the

[Read more →](https://thehackernews.com/2026/05/praisonai-cve-2026-44338-auth-bypass.html)

---

### How AI Hallucinations Are Creating Real Security Risks

**Published:** Thu, 14 May 2026 17:00:00 +0530  

AI hallucinations are introducing serious security risks into critical infrastructure decision-making by exploiting human trust through highly confident yet incorrect outputs. When an AI model lacks certainty, it doesn’t have a mechanism to recognize that. Instead, it generates the most probable response based on patterns in its training data, even if that response is inaccurate. These outputs

[Read more →](https://thehackernews.com/2026/05/how-ai-hallucinations-are-creating-real.html)

---

### Windows Zero-Days Expose BitLocker Bypasses And CTFMON Privilege Escalation

**Published:** Thu, 14 May 2026 14:55:50 +0530  

An anonymous cybersecurity researcher who disclosed three Microsoft Defender vulnerabilities has returned with two more zero-days involving a BitLocker bypass and a privilege escalation impacting Windows Collaborative Translation Framework (CTFMON).
The security defects have been codenamed YellowKey and GreenPlasma, respectively, by the researcher, who goes by the online aliases Chaotic Eclipse

[Read more →](https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html)

---

### New Fragnesia Linux Kernel LPE Grants Root Access via Page Cache Corruption

**Published:** Thu, 14 May 2026 12:36:15 +0530  

Details have emerged about a new variant of the recent Dirty Frag Linux local privilege escalation (LPE) vulnerability that allows local attackers to gain root access, making it the third such bug to be identified in the kernel within a span of two weeks.
Codenamed Fragnesia, the security vulnerability is tracked as CVE-2026-46300 (CVSS score: 7.8) and is rooted in the Linux kernel's XFRM

[Read more →](https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html)

---
