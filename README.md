# 🤖 Digital Twin Portfolio System

An autonomous portfolio backend and custom Discord bot built to manage, retrieve, and display my software engineering and game development projects. 

This repository houses the infrastructure for my "Digital Twin," connecting a conversational Discord interface with a web-based UI and a cloud database to host heavy 3D game assets, AR applications, and code repositories efficiently.

## 🛠️ Architecture & Tech Stack
* **Language:** Python
* **Frontend UI:** Streamlit (`app.py`, `design.py`)
* **Backend Bot:** Discord.py (`main_bot.py`)
* **Cloud Database & Storage:** Supabase (PostgreSQL)

## ✨ Core Features
* **Cloud Code Vault:** Utilizes Supabase to store project metadata, descriptions, and URLs for large external media (>5GB), keeping the local codebase lightweight.
* **Autonomous Querying:** The Discord bot securely fetches project data and media links from the Supabase database based on user prompts.
* **Responsive Web Dashboard:** A customized Streamlit web app that visualizes the portfolio data and provides an interactive UI for users without Discord access.
* **Secure Credential Management:** Built with strict `.gitignore` protocols to protect API keys and database tokens from public exposure.

## 📂 File Structure
* `main_bot.py` - Core logic and API integration for the Discord bot.
* `database.py` - Handles authentication and secure connections to the Supabase Postgres vault.
* `app.py` - Main execution file for the Streamlit web dashboard.
* `design.py` - UI layout, CSS styling, and component rendering for the frontend.

## 🔗 The Digital Twin Ecosystem
This system serves as the central hub for my development portfolio. Below are the live repositories managed by this architecture:

* **[VR Racing Simulation]** - *(Link coming soon)*
[AR Vehicle Customization App](https://github.com/chobukiri/AR-iOS-Automotive-Application)
* **[Escape from Mutation - FPS (Unreal Engine 5)]** - *(Link coming soon)*
* **[The Forest Promise - Interactive AR (Unity)]** - *(Link coming soon)*
