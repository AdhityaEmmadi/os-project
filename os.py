import streamlit as st

# Security check functions
def check_buffer_overflow(line):
    return any(keyword in line for keyword in ["strcpy(", "strcat(", "sprintf(", "gets("])

def check_sql_injection(line):
    return "execute(" in line and ("\"" in line or "'" in line)

def check_hardcoded_password(line):
    return "password" in line.lower() and ("\"" in line or "'" in line)

def check_insecure_functions(line):
    return any(keyword in line for keyword in ["system(", "popen(", "eval(", "exec("])

# Main scan function
def scan_code(file_content):
    warnings = []
    try:
        lines = file_content.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        return ["❌ Error decoding file. Please upload a text-based code file."]
    
    for lineno, line in enumerate(lines, start=1):
        if check_buffer_overflow(line):
            warnings.append(f"⚠️ **Buffer Overflow** risk on line {lineno}: `{line.strip()}`")
        if check_sql_injection(line):
            warnings.append(f"⚠️ **SQL Injection** risk on line {lineno}: `{line.strip()}`")
        if check_hardcoded_password(line):
            warnings.append(f"⚠️ **Hardcoded Password** found on line {lineno}: `{line.strip()}`")
        if check_insecure_functions(line):
            warnings.append(f"⚠️ **Insecure Function Usage** on line {lineno}: `{line.strip()}`")
    
    if not warnings:
        warnings.append("✅ No vulnerabilities detected.")
    
    return warnings

# Streamlit UI
st.set_page_config(page_title="Security Vulnerability Scanner", layout="centered")
st.title("🔐 Code Security Vulnerability Scanner")

st.markdown("""
Upload your source code file and this tool will scan it for basic security vulnerabilities.
Supports `.py`, `.c`, `.cpp`, `.java`, `.txt`, and similar code files.
""")

uploaded_file = st.file_uploader("📁 Upload your code file", type=["txt", "py", "c", "cpp", "java"])

if uploaded_file:
    st.subheader("🔍 Scan Results")
    results = scan_code(uploaded_file.read())
    for result in results:
        st.markdown(result)
