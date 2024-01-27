import streamlit as st

st.title("ラベル付与ページ")

if "text_on" not in st.session_state:
    st.session_state.text_on = False

if "text_lines_emp" not in st.session_state:
    st.session_state.text_lines_emp = []

if "text_lines" not in st.session_state:
    st.session_state.text_lines = []

if "labeled_lines" not in st.session_state:
    st.session_state.labeled_lines = []

# ユーザーからの新しい入力を取得
if not st.session_state.text_on:
    if input := st.text_area("入力してください"):
        st.session_state.text_lines_emp = input.split("\n")
        for line in st.session_state.text_lines_emp:
            if line:
                st.session_state.text_lines.append(line)
        st.session_state.text_on = True
else:
    st.header("ラベル付与")

    for line in st.session_state.text_lines:
        if line:
            st.subheader(line)
            options_char = ["", "syujinkou", "sei", "aki", "su", "hama", "seifes"]
            selected_option_char = st.selectbox(
                "キャラ:", options_char, key=line + "_char"
            )

            options_file = [
                "",
                "_a",
                "_b",
                "_d",
                "_f",
                "_h",
                "_n",
                "_q",
                "_s",
                "_sd",
                "_sh",
                "_sp",
                "_st",
                "_di",
                "_pn",
            ]
            selected_option_file = st.selectbox(
                "ファイルタグ:", options_file, key=line + "_file"
            )

            options_pos = ["", "c", "l", "r"]
            selected_option_pos = st.selectbox("位置:", options_pos, key=line + "_pos")

            options_bgm = [
                "",
                "stop",
                "seitheme",
                "akitheme",
                "suutheme",
                "Everyday",
                "myroom",
                "town",
                "fes",
                "fin",
                "title",
            ]
            selected_option_bgm = st.selectbox("BGM:", options_bgm, key=line + "_bgm")

            options_back = [
                "",
                "sky", 
                "white",
                "kyousitu_hiru",
                "kyousitu_yuu",
                "rouka_hiru",
                "rouka_yuu",
                "rouka_yoru_on",
                "rouka_yoru_off",
                "syoukou_hiru",
                "syoukou_yuu",
                "syoukou_yoru_on",
                "syoukou_yoru_off",
                "mati_hiru_ao",
                "mati_hiru_aka",
                "mati_yuu_ao",
                "mati_yuu_aka",
                "mati_yoru_ao",
                "mati_yoru_aka",
                "syoutengai_hiru",
                "syoutengai_yuu",
                "syoutengai_yoru",
                "heya_hiru",
                "heya_yuu",
                "heya_yoru_on",
                "heya_yoru_off",
                "stage_hiru",
                "stage_yuu",
                "stage_yoru",
                "sheet",
                "station",
            ]
            selected_option_back = st.selectbox("背景:", options_back, key=line + "_back")

            options_event = ["", "select", "daialogue_start", "attack_start", "attack_end", "trigger"]
            selected_option_event = st.selectbox(
                "イベント:", options_event, key=line + "_event"
            )

            options_scene1 = ["", "file"]
            selected_option_scene1 = st.selectbox(
                "シーン遷移1:", options_scene1, key=line + "_scene1"
            )

            options_scene2 = ["", "file"]
            selected_option_scene2 = st.selectbox(
                "シーン遷移2:", options_scene2, key=line + "_scene2"
            )

            labeled_text = f"{line},{selected_option_char},{selected_option_file},{selected_option_pos},{selected_option_bgm},{selected_option_back},{selected_option_event},{selected_option_scene1}{selected_option_scene2}"
            st.session_state.labeled_lines.append(labeled_text)

    if st.button("ラベリング結果を表示", key="_button"):
        st.text("ラベリング結果:")
        st.text(
            "\n".join(
                st.session_state.labeled_lines[-len(st.session_state.text_lines) :]
            )
        )
