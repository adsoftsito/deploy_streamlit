import streamlit as st
conn = st.connection("postgresql", type="sql")
if st.button("Query Postgresql table"):
    # Perform query.
    df = conn.query('SELECT * FROM people;', ttl="10m")
    # Print results.
    for row in df.itertuples():
        st.write(row)
