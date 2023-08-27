import streamlit as st

def display_about():
    st.title("About this Medical Bot")
    
    reasons = [
        "Comprehensive Medical Knowledge: With the vast amount of medical information available, it's challenging for both professionals and patients to stay updated. This app consolidates knowledge from various trusted sources, providing a one-stop solution.",
        "Bridging Conventional and Alternative Medicine: There's a growing interest in natural and herbal therapies. By integrating this knowledge with conventional treatments, the app offers a holistic approach to health.",
        "Enhancing Patient Autonomy: Empowering patients with knowledge allows them to make informed decisions about their health and fosters a collaborative doctor-patient relationship.",
        "Streamlining Medical Consultations: Healthcare professionals can utilize the app to quickly reference treatments, enhancing the efficiency and accuracy of consultations."
    ]
    for reason in reasons:
        st.markdown(f"- {reason}")
    
    # Use Cases
    st.header("Use Cases")
    cases = [
        "Symptom Checker: Users can input their symptoms and receive potential diagnoses, along with both conventional and natural treatment options.",
        "Drug-Herb Interactions: Before starting a new herbal remedy, users can check for potential interactions with their current medications.",
        "Treatment Deep Dive: Users can explore in-depth information about specific treatments, from surgical procedures to herbal therapies.",
        "Holistic Health Plans: Based on a user's medical history and preferences, the app can generate a holistic health plan that integrates conventional treatments with natural therapies.",
        "Continuous Learning: Medical professionals can use the app to stay updated on the latest research and treatment protocols in both conventional and alternative medicine."
    ]
    for case in cases:
        st.markdown(f"- {case}")
    
    # Why It's a Good Idea for the HealthUniverse Hackathon
    st.header("Why It's a Good Idea for the HealthUniverse Hackathon")
    points = [
        "Aligns with Hackathon Goals: The app addresses the hackathon's focus on innovative solutions in the healthcare domain, offering a unique approach to integrated medical knowledge.",
        "Addresses a Market Gap: While there are many medical reference apps, few seamlessly integrate conventional medicine with natural and herbal therapies.",
        "Scalability: The generative AI model can be continuously updated with new research and medical guidelines, ensuring the app remains relevant.",
        "Potential for Global Impact: With the rise of telemedicine and digital health platforms, this app has the potential to reach a global audience, democratizing access to integrated medical knowledge."
    ]
    for point in points:
        st.markdown(f"- {point}")
    
    # Value of Cross-Referencing Medical Knowledge
    st.header("Value of Cross-Referencing Medical Knowledge")
    values = [
        "Comprehensive Care: By integrating various medical disciplines, patients receive a more comprehensive care plan that addresses the root cause of ailments.",
        "Personalized Treatment: Cross-referencing allows for a more personalized approach, tailoring treatments to individual needs and preferences.",
        "Safety: Checking for drug-herb interactions and contraindications ensures that treatments are safe and effective.",
        "Empowerment: Providing users with a holistic view of their health empowers them to take charge of their well-being."
    ]
    for value in values:
        st.markdown(f"- {value}")
    
    # Conclusion
    st.header("Conclusion")
    st.markdown("""
    The Generative AI Medical Application is a pioneering solution in the realm of digital health. By seamlessly integrating diverse medical knowledge, it addresses the evolving needs of both patients and healthcare professionals. As healthcare continues to evolve, tools like this will be instrumental in shaping the future of integrative medicine.
    """)

