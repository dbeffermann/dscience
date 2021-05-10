#!/usr/bin/env python3
import pandas as pd
import streamlit as st
from instagramy.plugins.analysis import analyze_users_popularity
from instagramy import InstagramUser


def main():
	session_id = st.sidebar.text_input("@SessionId")

	user = st.sidebar.text_input("@User")

	button = st.sidebar.button("Run")

	url = "https://warehouse-camo.ingress.cmh1.psfhosted.org/53ef824d6e71053b3c1bf530da7004c04af479ee/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f796f67657368776172616e30312f696e7374616772616d792f6d61737465722f73616d706c65732f73657373696f6e69642e676966"
	st.sidebar.markdown(f'<a href="{url}" target = blank_>¿Cómo obtengo mi session id?</a>', unsafe_allow_html=True)

	if user and session_id:
	    try:
	        user_ = InstagramUser(user, from_cache=True)
	    except:
	        user_ = InstagramUser(user, sessionid= session_id)
	    st.write(user_.user_data)

if __name__ == '__main__':

	main()


