import streamlit as st

def show():
    st.title('🧑‍💻 การพัฒนาโมเดล Machine Learning และ Neural Network')

    st.markdown('<hr style="border: 1px solid #333;">', unsafe_allow_html=True)

    
    with st.expander("ขั้นตอนการพัฒนาโมเดล Machine Learning และ Neural Network"):
        st.markdown("""
        ### 1. การเตรียมข้อมูล
        - **การเก็บข้อมูล:** เก็บข้อมูลจากแหล่งต่างๆ เช่น ฐานข้อมูล หรือไฟล์ CSV
        - **การทำความสะอาดข้อมูล:** ตรวจสอบข้อมูลให้ถูกต้อง และจัดการค่าที่หายไป เช่น การแทนที่ค่าที่หายไป หรือการลบข้อมูลที่ไม่สมบูรณ์
        - **การสร้างคุณลักษณะ (Feature Engineering):** การแปลงข้อมูลหรือการสร้างคุณลักษณะใหม่ที่มีความสัมพันธ์กับตัวแปรเป้าหมาย เพื่อให้โมเดลเรียนรู้ได้ดีขึ้น
        """)

    with st.expander("อัลกอริธึม Machine Learning (ML)"):
        st.markdown("""
        ### 2. อัลกอริธึม Machine Learning (ML)
        - **ทฤษฎี:** อัลกอริธึม ML ทำการหาฟังก์ชันที่เชื่อมโยงข้อมูลอินพุตกับตัวแปรเป้าหมาย (ผลลัพธ์) โดยอาศัยการเรียนรู้จากข้อมูลที่มีอยู่
        - **ขั้นตอนการพัฒนา:**
            - **การแบ่งข้อมูล:** แบ่งข้อมูลเป็นชุดฝึกสอน (Training Set) และชุดทดสอบ (Test Set)
            - **การเลือกโมเดล:** เลือกโมเดลที่เหมาะสม เช่น Random Forest, Support Vector Machine (SVM), หรือ Decision Trees
            - **การฝึกโมเดล:** ใช้ข้อมูลฝึกสอนเพื่อหาค่าพารามิเตอร์ที่ดีที่สุด
            - **การประเมินผล:** ใช้การวัดผล เช่น Accuracy, Mean Squared Error (MSE) หรือ R-squared เพื่อตรวจสอบความแม่นยำของโมเดล
        """)

    with st.expander("อัลกอริธึม Neural Network (NN)"):
        st.markdown("""
        ### 3. อัลกอริธึม Neural Network (NN)
        - **ทฤษฎี:** Neural Network คือเทคนิคที่ได้รับแรงบันดาลใจจากการทำงานของสมอง ประกอบด้วยหลายชั้นของนิวรอนที่ประมวลผลข้อมูลและเรียนรู้จากการปรับค่าน้ำหนัก (Weights)
        - **ขั้นตอนการพัฒนา:**
            - **การออกแบบสถาปัตยกรรม:** กำหนดจำนวนชั้นและจำนวนของนิวรอนในแต่ละชั้น
            - **ฟังก์ชันการกระตุ้น (Activation Function):** ฟังก์ชันการกระตุ้นที่ใช้ เช่น ReLU หรือ Sigmoid เพื่อเพิ่มความซับซ้อนให้โมเดล
            - **ฟังก์ชันความสูญเสีย (Loss Function):** ใช้ฟังก์ชันความสูญเสีย เช่น Mean Squared Error (MSE) หรือ Cross-Entropy เพื่อวัดความคลาดเคลื่อนระหว่างผลลัพธ์ที่คาดการณ์กับค่าจริง
            - **การฝึกโมเดล:** ใช้ Backpropagation ในการปรับน้ำหนัก และใช้ Optimizer เช่น Adam เพื่อลดความสูญเสีย
            - **การประเมินผล:** ประเมินโมเดลโดยใช้ตัวชี้วัดเช่น Accuracy หรือ MSE บนชุดข้อมูลทดสอบ
        """)

    with st.expander("การเปรียบเทียบระหว่าง Machine Learning และ Neural Networks"):
        st.markdown("""
        ### 4. การเปรียบเทียบระหว่าง Machine Learning และ Neural Networks
        - **Machine Learning:** มักจะง่ายและรวดเร็วในการฝึกฝนและทำความเข้าใจ แต่จะไม่เหมาะสำหรับงานที่ซับซ้อน เช่น การจดจำภาพหรือเสียง
        - **Neural Networks:** ใช้ในการเรียนรู้รูปแบบที่ซับซ้อนและมีความสามารถในการจัดการกับข้อมูลจำนวนมากและซับซ้อน แต่ต้องการทรัพยากรมากกว่าและเวลาฝึกนานกว่า
        """)

    with st.expander("ขั้นตอนการพัฒนาโมเดลและการใช้งาน"):
        st.markdown("""
        ### 5. ขั้นตอนการพัฒนาโมเดลและการใช้งาน
        - **การโหลดข้อมูล:** ใช้ไลบรารีเช่น `pandas` ในการโหลดข้อมูลจากไฟล์ CSV และทำการเตรียมข้อมูล
        - **การแบ่งข้อมูล:** แบ่งข้อมูลเป็นชุดฝึกสอนและทดสอบ เพื่อประเมินผลของโมเดล
        - **การสร้างโมเดล (ML/NN):** ใช้การเลือกอัลกอริธึมเช่น Random Forest หรือสร้างโมเดล Neural Network ด้วย TensorFlow/Keras
        - **การฝึกฝนและการประเมินผล:** ฝึกโมเดลและใช้ตัวชี้วัดในการประเมิน เช่น Accuracy หรือ Mean Absolute Error (MAE)
        - **การปรับแต่งพารามิเตอร์:** ปรับแต่งพารามิเตอร์เพื่อเพิ่มประสิทธิภาพโมเดล
        """)

    with st.expander("การใช้งานและการนำไปใช้"):
        st.markdown("""
        ### 6. การใช้งานและการนำไปใช้
        - หลังจากที่ฝึกโมเดลเสร็จแล้ว คุณสามารถนำโมเดลไปใช้ในระบบจริง เช่น การสร้าง API หรือใช้เครื่องมืออย่าง **Streamlit** สำหรับการแสดงผลผ่านเว็บแอป
        """)

if __name__ == '__main__':
    show()