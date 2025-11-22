# Agri-Sahayak
Connecting Farmers ,Researchers ,Student and Markets with Generative AI

# 🌿 Agri-Sahayak: The Farmer-to-Researcher Generative AI Loop

[![Team: DATA FINDER'S](https://img.shields.io/badge/Team-DATA%20FINDER'S-brightgreen.svg)](https://github.com/your-team-repo)
[![Hackathon: Build With Gemini](https://img.shields.io/badge/Build%20With-Gemini-blue.svg)](https://ai.google.dev/gemini)
[![Theme: Social Good](https://img.shields.io/badge/Theme-Social%20Good%20%26%20Future%20of%20Work-orange.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌟 Project Overview

[cite_start]Agri-Sahayak is a unified, real-time platform designed to bridge the communication and data gap between **farmers**, **agricultural researchers**, and **students** in India[cite: 27]. [cite_start]Leveraging the Google **Gemini API**, the platform provides instant AI-powered crop disease diagnostics to farmers, while simultaneously feeding real-time, localized outbreak data to researchers for predictive modeling and targeted preventative action[cite: 36, 47, 54].

[cite_start]The project aims to combat significant crop loss (20-40%) due to misidentified diseases, counter the critical language barrier, and replace outdated educational materials with live, real-world field data[cite: 10, 12, 17, 19].

## ✨ Core Features

### 👨‍🌾 For Farmers
* [cite_start]**AI Disease Scanner:** Instant crop diagnosis by simply uploading a photo of an affected leaf or stem[cite: 32].
* [cite_start]**Localized, Actionable Reports:** Diagnosis includes suggested **CIBRC-approved remedies** and is delivered in their native language[cite: 33, 34, 49].
* [cite_start]**Knowledge Hub:** Access to an encyclopedia of crops, diseases, and treatments[cite: 33].

### 🔬 For Researchers
* [cite_start]**Live Outbreak Map:** Real-time national visualization of every farmer-uploaded scan, enabling immediate response to epidemics[cite: 36, 54].
* [cite_start]**Targeted Alerts:** Ability to send AI-translated preventative alerts to any 10km radius based on predictive models[cite: 37, 38].
* **Q&A Studio:** A dedicated space to review and answer farmer questions (reflected in `researcher.html` and `qa_questions`/`qa_answers` tables).

### 🎓 For Students
* [cite_start]**Academic Sandbox:** Read-only access to the Live Outbreak Map for real-world case studies and practical learning[cite: 40, 42].
* [cite_start]**Data Access:** Access to anonymized historical data for research projects[cite: 41].

## 🛠️ Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **AI/ML** | [cite_start]**Google Gemini Pro Vision & Gemini Pro API** [cite: 64] | [cite_start]Instant image analysis, diagnosis, and language translation[cite: 47, 49]. |
| **Backend** | [cite_start]**Python 3 & Flask** [cite: 75, 80] | Data pipeline, routing, session management, and API handling. |
| **Frontend** | [cite_start]HTML, CSS, JavaScript, **Bootstrap 5.3** [cite: 65, 66] | [cite_start]Single, mobile-first responsive web platform (PWA experience)[cite: 67]. |
| **Database** | [cite_start]**MySQL (via `schema.sql` definition)** [cite: 77, 85] | [cite_start]Robust storage for user profiles, uploads, diagnostics, and Q&A data[cite: 85]. |
| **Other** | `python-dotenv`, `datetime` | Configuration and utility functions. |

## 🚀 Getting Started

Follow these steps to set up the Agri-Sahayak application locally.

### Prerequisites

1.  **Python 3.x**
2.  A **Gemini API Key** (Get one from Google AI Studio)
3.  A **MySQL** database instance

### 1. Setup the Backend Environment

Clone the repository and install the required Python dependencies:

```bash
git clone [https://github.com/your-team-repo/agri-sahayak.git](https://github.com/your-team-repo/agri-sahayak.git)
cd agri-sahayak
pip install -r requirements.txt
