import streamlit as st
import time

# --- [1] 기억의 저장소 초기화 ---
# 리스트(List)문을 사용하여 등장인물들을 순차적으로 담을 공간을 마련합니다.
if 'characters' not in st.session_state:
    st.session_state.characters = []

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = True

if 'view_mode' not in st.session_state:
    st.session_state.view_mode = False

# --- 메인 화면 ---
if st.session_state.logged_in:
    st.title("🖋️ 창조주의 작업실: 등장인물 보관소")
    st.write("당신의 펜끝에서 태어난 영혼들에게 숨결을 불어넣으세요.")
    
    st.divider()

    # --- [2] 생명 부여 (입력) ---
    st.subheader("새로운 영혼 빚어내기")
    col1, col2 = st.columns(2)
    with col1:
        char_name = st.text_input("이름 (Name)")
        char_role = st.text_input("역할 (Role - 예: 주인공, 흑막)")
    with col2:
        char_age = st.text_input("나이 (Age)")
        char_trait = st.text_area("특징 및 비밀 (Traits & Secrets)")

    if st.button("✨ 등장인물 세계에 기록하기"):
        if char_name:
            # 딕셔너리 형태로 리스트에 추가합니다.
            new_soul = {
                "이름": char_name,
                "역할": char_role,
                "나이": char_age,
                "특징": char_trait
            }
            st.session_state.characters.append(new_soul)
            st.success(f"위대한 서사시에 '{char_name}'이(가) 성공적으로 아로새겨졌습니다.")
        else:
            st.warning("이름 없는 영혼은 존재할 수 없습니다. 이름을 지어주세요.")

    st.divider()

    # --- [3] 영혼의 전시 (순차적 리스트 보여주기) ---
    if st.button("👁️ 그동안 창조한 인물들 한눈에 보기"):
        st.session_state.view_mode = not st.session_state.view_mode

    if st.session_state.view_mode:
        st.subheader("📜 위대한 명부 (The Great Roster)")
        
        if len(st.session_state.characters) == 0:
            st.info("아직 이 세계에 태어난 인물이 없습니다.")
        else:
            # 리스트를 순회하며 보기 좋게 출력합니다.
            for index, char in enumerate(st.session_state.characters):
                with st.container():
                    st.markdown(f"### {index + 1}. {char['이름']} ({char['역할']})")
                    st.write(f"**나이:** {char['나이']}")
                    st.write(f"**특징 및 비밀:** {char['특징']}")
                    
                    # --- [4] 소멸의 권리 (If문 사용) ---
                    # If문을 사용하여 이 버튼이 눌렸을 때만 삭제 로직이 작동하게 합니다.
                    if st.button(f"❌ '{char['이름']}'의 존재를 세계에서 지우기", key=f"delete_{index}"):
                        deleted_name = st.session_state.characters[index]['이름']
                        del st.session_state.characters[index]
                        st.error(f"'{deleted_name}'의 존재가 안개처럼 사라졌습니다.")
                        st.rerun()
                st.write("---")

    st.divider()

    # --- [5] 작업실 퇴장 ---
    if st.button("🚪 작업실 나가기 (로그아웃)"):
        st.session_state.logged_in = False
        st.rerun()

# --- [6] 이별의 의식 (While문 사용) ---
# 사용자가 로그아웃을 시도했을 때 실행되는 구역입니다.
else:
    st.title("🌙 작업실의 불이 꺼집니다...")
    st.write("마지막으로 창조된 영혼이 안전하게 기록되는지 확인합니다.")
    
    save_completed = False
    verification_steps = 0
    
    # While문을 사용하여 마지막 캐릭터의 정보가 안전하게 저장되는 과정을 시뮬레이션합니다.
    while not save_completed:
        time.sleep(1) # 1초 대기 (저장하는 연출)
        verification_steps += 1
        
        if verification_steps == 1:
            if len(st.session_state.characters) > 0:
                last_char = st.session_state.characters[-1]['이름']
                st.info(f"마지막으로 남겨진 영혼 '{last_char}'의 정보를 영원의 서판에 옮겨 적는 중입니다...")
            else:
                st.info("기록할 영혼이 존재하지 않습니다. 빈 양피지를 덮습니다...")
                
        elif verification_steps == 2:
            st.warning("먼지가 쌓이지 않도록 세계의 문을 단단히 봉인하는 중...")
            
        elif verification_steps >= 3: # 3번의 확인 과정이 끝나면 루프를 탈출합니다.
            save_completed = True
            
    st.success("모든 기록이 안전하게 보존되었습니다. 창조주여, 편히 쉬소서. (새로고침을 눌러 다시 돌아오세요)")
    