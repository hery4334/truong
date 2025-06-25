import streamlit as st
from PIL import Image
from auth import login
from utils import load_products

# Giao diện đăng nhập
if not login():
    st.stop()

# Tải dữ liệu
products = load_products()

# Giao diện chính
st.title("🛒 Cửa Hàng Thương Mại Điện Tử")
category = st.sidebar.selectbox("🎯 Chọn danh mục", ["Tất cả"] + list(set(p["category"] for p in products)))
search = st.sidebar.text_input("🔍 Tìm kiếm sản phẩm")

if "cart" not in st.session_state:
    st.session_state.cart = []

filtered_products = [p for p in products if
                     (category == "Tất cả" or p["category"] == category) and
                     (search.lower() in p["name"].lower())]

cols = st.columns(3)
for i, product in enumerate(filtered_products):
    with cols[i % 3]:
        st.image(product["image"], use_column_width=True)
        st.markdown(f"**{product['name']}**")
        st.caption(product["description"])
        st.markdown(f"💵 Giá: {product['price']:,}đ")
        if st.button(f"🛒 Mua - {product['name']}", key=product["name"]):
            st.session_state.cart.append(product)
            st.success("Đã thêm vào giỏ hàng.")

st.markdown("---")
st.markdown("### 🧺 Giỏ hàng")

if st.session_state.cart:
    total = 0
    for item in st.session_state.cart:
        st.write(f"✔️ {item['name']} - {item['price']:,}đ")
        total += item["price"]
    st.markdown(f"**Tổng cộng: {total:,}đ**")
    if st.button("🧹 Xóa giỏ hàng"):
        st.session_state.cart = []
else:
    st.info("Giỏ hàng của bạn đang trống.")
