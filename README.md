# 📱 Appium Automation Testing Mobile Posaja

Automated mobile testing framework for Android using **Appium** + **WebdriverIO** with JavaScript.

---

## ✨ Key Features

- **Appium 2.x** — Latest mobile automation framework
- **WebdriverIO** — Modern test runner with mocha
- **Page Object Model** — Clean, maintainable test architecture
- **Allure Reports** — Beautiful, detailed test reports
- **UiAutomator2** — Native Android automation driver
- **Auto Screenshot** — Captures screenshots on failure

---

## 📁 Project Structure

```
appium-mobile-automation/
├── tests/
│   └── logs/
│   └── screenshot/
├── ordercod.py
├── orderccod.py
├── ordernoncod.py
├── orderccodpoin.py
├── orderdropoff.py
└── README.md
```

---

## ⚙️ Prerequisites

| Software | Version | Download |
|----------|---------|----------|
| **Node.js** | 18+ | [nodejs.org](https://nodejs.org/) |
| **Java JDK** | 11+ | [adoptium.net](https://adoptium.net/) |
| **Android Studio** | Latest | [developer.android.com](https://developer.android.com/studio) |
| **Appium** | 2.x | Installed via npm |

### Environment Variables

```bash
ANDROID_HOME=/path/to/android/sdk
JAVA_HOME=/path/to/java/jdk
```

### Download Test App

Download **ApiDemos-debug.apk** and place it in the `apps/` folder:
- [ApiDemos APK](https://github.com/appium/android-apidemos/releases)

---

## 🚀 Getting Started

### 1. Clone & Install

```bash
git clone https://github.com/agungprakasa/Automation-Testing-Mobile-Posaja.git
cd Automation-Testing-Mobile-Posaja
npm install
```

### 2. Start Appium Server

```bash
npx appium
```

### 3. Start Android Emulator

```bash
# List available AVDs
emulator -list-avds

# Start emulator
emulator -avd <your_avd_name>
```

### 4. Run Tests

```bash
# Run all tests
npm test

# Run specific test
npm run test:login
npm run test:navigation
npm run test:form
```

### 5. View Allure Reports

```bash
npx allure generate allure-results --clean
npx allure open
```

---

## 📊 Test Coverage

| # | Feature | File | TCs | Scenarios |
|---|---------|------|-----|-----------|
| 1 | Login & Order | All | 10 | Login & Order |
| | **Total** | | **10** | |

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| **Appium 2.x** | Mobile automation framework |
| **WebdriverIO** | Test runner |
| **UiAutomator2** | Android automation driver |
| **Mocha** | Test framework |
| **Allure** | Test reporting |
| **JavaScript** | Programming language |

---

## 👤 Author

**Agung Prakasa** — [GitHub](https://github.com/agungprakasa)

---
