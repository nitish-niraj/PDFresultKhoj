
## PDFResultKhoj v1.5

Live Demo: [https://pdfresultkhoj.onrender.com/](https://pdfresultkhoj.onrender.com/)

---

### Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture & Tech Stack](#architecture--tech-stack)
4. [Getting Started](#getting-started)
   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
   * [Running Locally](#running-locally)
5. [Usage](#usage)
   * [Search Interface](#search-interface)
   * [Search Modes](#search-modes)
   * [Example Queries](#example-queries)
6. [Directory Structure](#directory-structure)
7. [Deployment](#deployment)
   * [Render.com Setup](#rendercom-setup)
   * [Custom Domain](#custom-domain)
8. [Extending & Contributing](#extending--contributing)
9. [Roadmap & Future Enhancements](#roadmap--future-enhancements)
10. [License](#license)

---

## Project Overview

**PDFResultKhoj** is a web-based tool that enables students to instantly search their exam results across large, multi-PDF listing files. Users can enter a roll number, candidate’s name, or father’s name to retrieve full result details in under a second, eliminating the need to manually scroll through hundreds of pages.

---

## Features

* 🔄 **Multi-PDF Batch Import**: Combine multiple PDF result files into a single searchable CSV.
* 🔍 **Multi-Field Search**: Search by roll number (exact), candidate name (partial, case-insensitive), or father’s name (partial, case-insensitive).
* ⚡ **High Performance**: Preprocessed CSV lookup (<50 ms on 600k+ records).
* 📄 **Full Detail Display**: Shows Roll, Name, Father, Mother, Category Code, and Source File.
* 🌐 **Live-Web Deployment**: Hosted on Render.com, mobile-responsive, zero-config.
* 🛡️ **Secure Input Handling**: All user inputs are sanitized to prevent injection attacks.
* 📝 **Extensible Backend**: Easily add new fields or search modes.
* 🐳 **Docker Support**: (Optional) Dockerfile for containerized deployment.

---

## Architecture & Tech Stack

| Layer               | Technology              |
| ------------------- | ----------------------- |
| **Data Extraction** | Python + PyMuPDF        |
| **Preprocessing**   | Python CSV library      |
| **Backend**         | Python + Flask          |
| **Frontend**        | HTML5, CSS3, Vanilla JS |
| **Hosting**         | Render.com              |
| **Version Control** | Git + GitHub            |
| **Containerization**| Docker (optional)       |

---

## Getting Started

### Prerequisites

* Python 3.8+
* `pip` package manager
* Git
* (Optional) Docker

### Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/PDFResultKhoj.git
   cd PDFResultKhoj
   ```

2. **Create & activate a virtualenv**

   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. **Convert your PDFs** (if you haven’t already):

   ```bash
   python combine_pdfs.py
   ```

   This reads `data/raw_pdfs/*.pdf` and writes `data/data.csv`.

2. **Start the Flask app**

   ```bash
   python app.py
   ```

3. **Open your browser** at `http://localhost:5000`

#### (Optional) Run with Docker

```bash
docker build -t pdfresultkhoj .
docker run -p 5000:5000 pdfresultkhoj
```

---

## Usage

### Search Interface

* **Roll Number** (exact match)
* **Candidate’s Name** (partial, case-insensitive)
* **Father’s Name** (partial, case-insensitive)

Fill one or more fields and hit **Search**.

### Search Modes

| Mode            | Behavior                                       |
| --------------- | ---------------------------------------------- |
| Roll only       | Finds exact roll match                         |
| Name only       | Lists all candidates whose names contain query |
| Father only     | Lists all whose father’s name contains query   |
| Combined fields | Narrows by all filled criteria                 |

### Example Queries

| Input                             | Output                                   |
| --------------------------------- | ---------------------------------------- |
| Roll: `3206063292`                | Single matching record                   |
| Name: `PRIYANSHU KUMAR`           | All “PRIYANSHU KUMAR” entries            |
| Name: `RAUSHAN` + Father: `SUDHA` | Only Raushan Kumar whose father is Sudha |

---

## Directory Structure

```
PDFResultKhoj/
├── app.py                   # Flask web server
├── combine_pdfs.py          # Batch PDF→CSV converter
├── data/
│   ├── raw_pdfs/            # Put your result PDFs here
│   └── data.csv             # Generated data file
├── requirements.txt         # Python deps
├── static/
│   ├── css/styles.css       # UI styles
│   └── js/scripts.js        # (optional) client scripts
├── templates/
│   └── index.html           # Search page template
├── Dockerfile               # (optional) for containerization
├── README.md                # This documentation
└── .gitignore
```

---

## Deployment

### Render.com Setup

1. **Connect GitHub repo** to Render.
2. **Create New Web Service**:
   * Root: `PDFResultKhoj/`
   * Build Cmd: `pip install -r requirements.txt`
   * Start Cmd: `python app.py`
3. **Deploy** and note your live URL.

Your app is now at `https://pdfresultkhoj.onrender.com/`.

### Custom Domain

1. In Render dashboard, go to **Settings → Custom Domains**
2. Add `pdfresultkhoj.in` (or your chosen domain)
3. Copy the provided CNAME → add to your DNS provider.
4. Wait for propagation (~5 min).

---

## Extending & Contributing

1. **Fork & Clone** the repo
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit** your changes, **Push**, and open a **Pull Request**.
4. Suggestions welcome for:

   * Pagination of results
   * PDF upload admin UI
   * Live-search (AJAX)
   * Dockerfile / Kubernetes deployment
   * Additional search fields (e.g., Mother’s Name, Category)
   * Export results as PDF

---

## Roadmap & Future Enhancements

* **v1.1**: Live search (as-you-type) via AJAX
* **v1.2**: Pagination & result download CSV export
* **v2.0**: Authentication & role-based access (admin & student)
* **v3.0**: Multi-exam support & result analytics dashboard
* **v3.1**: PDF upload via web UI
* **v3.2**: Export search results as PDF

---

## License

MIT License © 2025 PDFResultKhoj Contributors

---

> **Enjoy building — and happy searching!**
> सुणकि बहुत अच्छा लगा, आप भी अपना ख्याल रखें।
