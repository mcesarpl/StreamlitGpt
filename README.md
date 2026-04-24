# StreamlitGpt
This code builds a ChatGPT-style chat application using Streamlit, maintaining conversation state and interacting with the OpenAI API via streaming for real-time responses.

## 🚀 Streamlit — Quick Overview

![Streamlit Example](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)

**Streamlit** is a Python library that turns scripts into interactive web apps — no frontend required.

You write Python → it renders a UI automatically.

---

## ⚙️ How it works

- The script runs **top to bottom**
- On every user interaction, the app **reruns entirely**
- State is preserved using `st.session_state`

**Mental model (for JS/TS devs):**
- `st.*` ≈ UI components
- `session_state` ≈ global state (like React state + persistence)
- rerun behavior ≈ automatic re-render

---

## ✨ Advantages

- No frontend needed (no React, HTML, or CSS)
- Extremely fast prototyping
- Great for AI apps, dashboards, and internal tools
- Simple deployment

---

## ⚠️ Limitations

- Not ideal for complex production UIs
- Full rerun model can feel unusual at first
- Limited scalability compared to traditional backends

---

## 🧩 Minimal example

```python
import streamlit as st

st.title("Hello world")

name = st.text_input("Your name")

if name:
    st.write(f"Hello, {name} 👋")