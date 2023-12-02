import streamlit as st
import convector as cvt

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def show_result(df):
    c1, c2, c3 = st.columns(3)
    with c2:
        st.dataframe(df, hide_index = True, width = 450)
def init():
    local_css("style.css")

    if 'unit' not in st.session_state:
        st.session_state['unit'] = 'none'

    st.title("Конвектор единиц веса")
    st.write("Единица измерения исходного числа")

    kg, gr, lb, oz = st.columns(4)
    with kg:
        kg_btn = st.button("Кг")
        if kg_btn:
            st.session_state.unit = 'kg'
    with gr:
        gr_btn = st.button("Гр")
        if gr_btn:
            st.session_state.unit = 'gr'
    with lb:
        lb_btn = st.button("Lb")
        if lb_btn:
            st.session_state.unit = 'lb'
    with oz:
        oz_btn = st.button("Oz")
        if oz_btn:
            st.session_state.unit = 'oz'

    value = st.number_input("Введеите значение ", 0)

    btn = st.button("Перевести",type="primary")
    if btn:
        unit = st.session_state.unit
        st.write(f"{value} {unit} -")
        show_result(cvt.distribution_unit(unit, value))

        # if unit == "kg":
        #     st.write(f"{value} кг -")
        #     show_result(cvt.convert_weight_kg(value))

        # match st.session_state.unit:
        #     case 'kg':
        #         st.write(f"{value} кг -")
        #         show_result(cvt.convert_weight_kg(value))
        #     case 'gr':
        #         st.write(f"{value} грамм -")
        #         show_result(cvt.convert_weight_grams(value))
        #     case 'lb':
        #         st.write(f"{value} фунтов -")
        #         show_result(cvt.convert_weight_pounds(value))
        #     case 'oz':
        #         st.write(f"{value} унций -")
        #         show_result(cvt.convert_weight_ounces(value))
        #     case 'none':
        #         st.warning("Выберете единицу веса измрения исходного значения", icon="⚠️")


if __name__ == "__main__":
    init()
