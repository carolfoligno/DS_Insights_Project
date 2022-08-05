mkdir -p ~/.streamlit/

echo "\
[general]\n\
email=\"folignocaroline@gmail.com\"\n\
"> ~/.streamlit/credentials.toml

echo "\
[serve]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
"> ~/.streamlit/config.toml