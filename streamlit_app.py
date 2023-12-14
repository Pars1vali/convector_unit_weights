import streamlit as st
import convector as cvt

#метод загрузки стилей для элементов из файла style.css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
@st.cache_data
def show_result(df):
    c1, c2, c3 = st.columns(3)
    with c2:
        st.dataframe(df, hide_index = True, width = 400)
def init():
    #вызов метода загрузки стилей
    local_css("style.css")

    #инициализирем переменную unit в состоянии сеанса
    if 'unit' not in st.session_state:
        st.session_state['unit'] = 'none'

    #заголовок страницы
    st.title("Конвектор единиц веса")
    #объяснительная записка для ввода чисел
    st.write("Единица измерения исходного числа")

    #столбцы, где будут содержаться кнопки для выбора типа изначального значения с сохранением выбранного типа значения
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

    #целочисленный ввод значения
    value = st.number_input("Введеите значение ", 0)

    #кнопка для вызова запуска расчёта
    btn = st.button("Перевести",type="primary")
    #если кнопка нажата
    if btn:
        #переменная хранящая тип изначального значения
        unit = st.session_state.unit
        #предупрждение если тип не выбран
        if unit == 'none':
            st.warning("Выберете единицу веса измрения исходного значения", icon="⚠️")
        else:
            #вывод ориганльного значения и типа
            st.write(f"{value} {unit} -")
            #покать результат конвертирования числа после вызова соотвествующего метода из файла convert
            show_result(cvt.distribution_unit(unit, value))

#при запуске метода main вызвать функция для инициализации web-интерфейса
if __name__ == "__main__":
    init()
