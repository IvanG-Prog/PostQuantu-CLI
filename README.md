# 🛡️ PostQuantu CLI

[![Product Page](https://img.shields.io/badge/OFFICIAL_SITE-GET_CLI_HERE-3B82F6?style=for-the-badge)](https://ivang-prog.github.io/PostQuantu-CLI)

This is the **PostQuantu Command-Line Interface (CLI)**, designed as a robust and future-proof solution in the field of **Post-Quantum Cryptography (PQC)**. It leverages NIST-standardized algorithms (such as Kyber and Dilithium) to provide production-grade security and key management capabilities.

---

## ⬇️ Installation for End-Users (Recommended)

The easiest way to use the PostQuantu CLI is by downloading the **native installation package** for your operating system from the **Releases** page.

1.  **Download the Package:**
    Visit the dedicated **[Releases page](https://github.com/IvanG-Prog/PostQuantu-CLI/releases/tag/v1.0.0)** and download the latest version.
    * **Linux (Ubuntu/Debian):** Download the **`postquantu-cli_1.0.0_amd64.deb`** file.

2.  **Install and Run:**
    * **Double-click** the `.deb` file to install it using your system's software manager.
    * The application will appear in your application menu as **"PostQuantu CLI"**.

---

### 🛠️ Installation (Local Development Mode)

These steps allow **developers** to install the CLI in a virtual environment to **work, test, and modify the source code directly.**

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/IvanG-Prog/PostQuantu-CLI.git](https://github.com/IvanG-Prog/PostQuantu-CLI.git)
    cd PostQuantu-CLI
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python3 -m venv venv
    ```
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Install the project in Editable Mode:**
    ```bash
    pip install -e .
    ```

---

## 🚀 CLI Usage

Once installed, you can execute the primary command, **`postquantu`**, directly from any terminal session.

To launch the main menu:

    postquantu .
    