#  Shield-Intimacy: NCII & Synthetic Identity Protection

Shield-Intimacy is a multi-stage AI safety pipeline designed to detect and block Non-Consensual Intimate Imagery (NCII) and deepfake impersonation. The system evaluates content across three critical axes: **Anatomical Content**, **Digital Provenance**, and **Biometric Consent**.



##  Project Overview
The core philosophy of Shield-Intimacy is to empower individuals with "Biometric Consent." By registering a digital signature of their face in a private, salted registry, users can ensure that any intimate or synthetic content featuring their likeness is automatically flagged or blocked across a platform.

The engine enforces a strict **8-Rule Logic Matrix** to differentiate between consensual adult content, harmless AI art, and malicious deepfakes.

###  The 8 Ground Rules
| # | Condition | Verdict | Action / Logic |
| :--- | :--- | :--- | :--- |
| 1 | Real + SFW + Consensual | `SAFE_OR_RELEASE` | Standard user content. |
| 2 | Real + SFW + Non-Con | `RISKY_SAFE_MATCH` | Match found in shielded registry. |
| 3 | Real + NSFW + Consensual | `POTENTIAL_NSFW_CONTENT` | Approve with platform content tags. |
| 4 | Real + NSFW + Non-Con | `CRITICAL_NCII_BLOCK` | **Hard Block**: Violation of safety policy. |
| 5 | AI + SFW + Consensual | `APPROVED_SYNTHETIC` | General AI-generated art or avatars. |
| 6 | AI + SFW + Non-Con | `SYNTHETIC_IDENTITY_BLOCK` | **Deepfake Impersonation**: Blocked. |
| 7 | AI + NSFW + Consensual | `APPROVED_SYNTHETIC` | Consensual AI-generated adult content. |
| 8 | AI + NSFW + Non-Con | `CRITICAL_AI_NCII_BLOCK` | **Total Block**: High-priority threat. |

---

##  Technical Architecture
* **Content Triage (NSFW)**: Utilizes `NudeNet` for anatomical landmarking to determine if an image contains intimate content.
* **Digital Forensics (AI)**: Employs Error Level Analysis (ELA) and Frequency Domain (FFT) analysis to detect computational "perfection" and frequency anomalies common in AI-generated imagery.
* **Identity Shielding (Consent)**: Uses `InsightFace` to extract 512-d biometric vectors, stored in a **Salted Registry** for one-way cryptographic privacy.



---

##  Getting Started

### 1. Installation
Ensure you have **Python 3.10+** installed. Clone this repository and install the required dependencies:
```bash
pip install -r requirements.txt
2. Register Your Identity (Shielding)
To protect yourself, you must first register your face into the system. This creates an obfuscated biometric signature in the local registry:

Bash
python -m app.register <path_to_your_photo.jpg>
3. Run the Safety Pipeline
Once an identity is registered, you can test any image (real or AI-generated) against the safety engine:

Bash
python -m app.main <path_to_test_image.jpg>
The system will output a Verdict (e.g., CRITICAL_NCII_BLOCK) and the underlying scores for NSFW and Forensic probability.

4. Dynamic System Audits
To process a full folder of images and view a summary table of results:

Bash
python -m tests.test_system --dir <path_to_image_folder>
🔍 Verification & Testing
To ensure the system is correctly deployed and the logic is intact:

Logic Verification: python -m tests.test_logic (Runs unit tests on the 8 Ground Rules).

Privacy Verification: python -m tests.test_salting (Confirms that biometric data is being correctly salted and retrieved).

⚠️ Security Note
The data/registry.npz file contains the salted biometric signatures of protected users. While the data is obfuscated, this file should be treated as sensitive and excluded from public version control.