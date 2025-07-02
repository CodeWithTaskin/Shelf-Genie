# 📚 ShelfGenie – A Production-Grade Book Recommendation System

> **An end-to-end MLOps web application built entirely from scratch – designed to showcase real-world engineering, not just machine learning.**

---

<video src="assets/Recording 2025-07-01 170243.mp4" width="640" height="480" controls></video>

---

## 🚀 Project Overview

**ShelfGenie** isn’t just a machine learning model in a Jupyter notebook.  
It’s a full-stack, production-ready **MLOps ecosystem** designed to demonstrate real-world deployment, system architecture, and scalability.  

With a modern frontend, dynamic book recommendations, and an enterprise-level pipeline deployed on Azure, this app is the kind of portfolio project that doesn't just *talk* — it *ships*.

---

## ✨ Features & Highlights

- 🔍 **Top 100 Books on Landing Page**
- 📖 **Book Detail Page** with metadata and recommendation context
- 🔁 **Dynamic Recommendation Engine**: Suggests 20 similar books per selection — with recursive exploration
- 🔧 **Built Entirely from Scratch** – No prebuilt libraries or tools like DVC
- 🧱 **Modular, Scalable Architecture** following MLOps best practices
- 🧪 **End-to-End ML Pipeline** with:
  - Data Ingestion
  - Data Validation
  - Data Transformation
  - Model Training
  - Model Deployment (Dockerized)
- ☁️ **Cloud-Native Deployment on Azure**
- ⚙️ **CI/CD Automation** using GitHub Actions
- 🧪 **Multi-Stage Docker** for optimized image size
- 🧠 **MongoDB Integration** for tracking interactions
- 🎨 **Clean, Animated, Responsive Frontend** hosted on Cloudflare
- 🌐 **API-first Architecture** using Flask, integrated with the frontend

---

## 🧰 Tech Stack

| Category            | Technologies Used                                     |
|---------------------|--------------------------------------------------------|
| **Frontend**        | HTML/CSS, JavaScript, Animated UI, Cloudflare Pages    |
| **Backend**         | Python, Flask (REST API), MongoDB                     |
| **MLOps**           | Custom ML pipeline, Modular Design, Azure DevOps       |
| **Cloud & DevOps**  | Azure VM, Azure Blob Storage, Azure ACR, GitHub Actions |
| **Containerization**| Docker, Multi-Stage Build                              |
| **CI/CD**           | GitHub Actions                                         |
| **Hosting**         | Flask API on Render (Demo), Frontend on Cloudflare     |

---

## 🛠️ Installation & Usage

> Clone the repo and run locally using Docker or access the hosted demo (link below).

### 🔄 Clone & Run

```bash
git clone https://github.com/your-username/shelfgenie.git
cd shelfgenie
docker build -t shelfgenie-app .
docker run -p 8000:8000 shelfgenie-app
````

Visit: [http://localhost:8000](http://localhost:5000)

> 💡 You’ll need valid Azure credentials set in your environment variables or `.env` file for full cloud interaction.

---

## 🧪 API & Architecture Overview

**Core Components:**

```
📦 src/
├── data_ingestion/
├── data_validation/
├── data_transformation/
├── model_training/
├── model_pusher/
├── api/                  → Flask-based REST API
├── azure/                → Blob Storage, ACR, VM integration
└── cicd/                 → GitHub Actions workflow
```

* **Frontend** communicates with Flask backend via clean API endpoints.
* **Backend** serves model predictions, recommendations, and metadata via RESTful APIs.
* **CI/CD** automates build/test/deploy across Azure services using GitHub Actions.

---

## 🌍 Live Demo (Optional)

> 🔗 **Frontend**: [https://shelfgenie.pages.dev](https://shelf-genie.pages.dev)
> 🔗 **API (Render)**: [https://api-recommendation-system.onrender.com](https://api-recommendation-system.onrender.com)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.

---

## 🪪 License

Distributed under the **LGNU License**. See `LICENSE` for more information.

---

## 👤 About Me – Farjhan Ahmed

I'm a passionate Machine Learning Engineer focused on building production-level MLOps solutions with real-world architecture, cloud-native design, and full-stack integration.

> 🧠 I don’t just build models. I build systems.
> 💼 I’m actively looking for remote opportunities where I can bring this level of depth and execution to your team.
> 🤝 Open to collaboration, contract roles, or full-time ML/MLOps engineering work.

📫 **Connect with me**:

* LinkedIn: [linkedin.com/in/farjhan](https://linkedin.com/in/farjhan)
* Email: [farjhan.dev@gmail.com](mailto:farjhan.dev@gmail.com)
* Portfolio Website: *Coming soon*

---

## 🧠 Why This Project Matters

Recruiters, if you're reading this:

> This isn't another Kaggle clone. This is a **production-grade, cloud-deployed, CI/CD-enabled**, API-integrated **machine learning product** — built solo, from scratch.

If you're looking for engineers who don’t just know ML, but understand how to deploy, scale, and integrate it — let’s talk.

---
