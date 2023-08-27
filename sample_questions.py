import streamlit as st

def display_sample_questions():
    st.title("Sample Questions")

    role_plays = [
        {
            "title": "Role-play: Family Physician & Concerned Spouse",
            "prompt": 'Spouse: "My wife has been experiencing hot flashes and mood swings. What could be the reason, and are there any natural and herbal remedies?"'
        },
        {
            "title": "Role-play: Nutritionist & Fitness Enthusiast",
            "prompt": 'Enthusiast: "I\'ve been trying to bulk up but struggle with muscle recovery. Are there any dietary supplements or herbs that can aid in muscle repair and growth?"'
        },
        {
            "title": "Role-play: Herbalist & Traveler",
            "prompt": 'Traveler: "I often face jet lag when I travel across time zones. Are there any herbal remedies that can help me adjust my body clock naturally?"'
        },
        {
            "title": "Role-play: Surgeon & Anxious Patient",
            "prompt": 'Patient: "I\'m scheduled for a knee replacement surgery. Can you explain the procedure and any natural therapies I can consider for post-operative care?"'
        },
        {
            "title": "Role-play: Lab Technician & Curious Individual",
            "prompt": 'Individual: "I recently had a blood test that showed elevated liver enzymes. What does this mean, and are there any herbs known to support liver health?"'
        },
        {
            "title": "Role-play: Dietician & Diabetic Patient",
            "prompt": 'Patient: "I have type 2 diabetes. Are there any natural foods or herbs that can help regulate my blood sugar levels?"'
        },
        {
            "title": "Role-play: Pharmacist & Holistic Believer",
            "prompt": 'Believer: "I\'m on medication for hypertension. Are there any natural or herbal alternatives that can complement my current treatment?"'
        },
        {
            "title": "Role-play: Oncologist & Hopeful Patient",
            "prompt": 'Patient: "I\'m undergoing chemotherapy for breast cancer. Are there any natural remedies or herbs that can alleviate the side effects of the treatment?"'
        },
        {
            "title": "Role-play: Pediatrician & Concerned Parent",
            "prompt": 'Parent: "My child has ADHD. I\'ve heard about natural remedies that can help. Can you provide some insights into this?"'
        },
        {
            "title": "Role-play: Gastroenterologist & Foodie",
            "prompt": 'Foodie: "I love spicy foods, but lately, I\'ve been experiencing heartburn. Are there any natural or herbal remedies that can soothe my stomach?"'
        },
        {
            "title": "Role-play: Dermatologist & Beauty Enthusiast",
            "prompt": 'Enthusiast: "I have acne-prone skin. Are there any herbs or natural remedies that can help clear my skin?"'
        },
        {
            "title": "Role-play: Neurologist & Aging Individual",
            "prompt": 'Individual: "I\'ve been feeling forgetful lately. Are there any natural supplements or herbs that can boost brain health and memory?"'
        },
        {
            "title": "Role-play: Rheumatologist & Active Senior",
            "prompt": 'Senior: "I have arthritis in my hands. Are there any natural therapies or herbs that can help reduce the inflammation and pain?"'
        },
        {
            "title": "Role-play: Endocrinologist & Young Adult",
            "prompt": 'Adult: "I have been diagnosed with PCOS. Are there any natural remedies or herbs that can help manage the symptoms?"'
        },
        {
            "title": "Role-play: Cardiologist & Fitness Trainer",
            "prompt": 'Trainer: "I want to recommend natural supplements to my clients for heart health. Are there any herbs that can support cardiovascular function?"'
        },
        {
            "title": "Role-play: Pulmonologist & Smoker",
            "prompt": 'Smoker: "I\'ve been smoking for years and want to improve my lung health. Are there any herbs or natural remedies that can help cleanse my lungs?"'
        },
        {
            "title": "Role-play: Urologist & Middle-aged Man",
            "prompt": 'Man: "I have been facing issues with urinary health. Are there any natural remedies or herbs that can support prostate and urinary tract health?"'
        },
        {
            "title": "Role-play: Psychiatrist & Stressed Individual",
            "prompt": 'Individual: "I\'ve been feeling anxious and depressed. Are there any natural or herbal remedies that can help elevate my mood and reduce anxiety?"'
        },
        {
            "title": "Role-play: Ophthalmologist & Bookworm",
            "prompt": 'Bookworm: "I read a lot and lately, I\'ve been experiencing eye strain. Are there any natural remedies or herbs that can support eye health?"'
        },
        {
            "title": "Role-play: Orthopedic & Athlete",
            "prompt": 'Athlete: "I had a ligament tear last year. Are there any herbs or natural supplements that can strengthen my ligaments and prevent future injuries?"'
        },
        {
            "title": "Inquiry: Hypertension Medications & Herbal Remedies",
            "prompt": 'Discuss the potential interactions between conventional medications for hypertension and herbal remedies like hawthorn and garlic.'
        },
        {
            "title": "Nutrition & Medication: Diabetes Management",
            "prompt": 'How do dietary choices, especially the consumption of cinnamon and bitter melon, impact the efficacy of insulin and other diabetes medications?'
        },
        {
            "title": "Herbal Remedies & Chemotherapy",
            "prompt": 'Explain the implications of using herbal remedies like turmeric and milk thistle while undergoing chemotherapy treatments.'
        },
        {
            "title": "Antidepressants & Natural Mood Enhancers",
            "prompt": 'Detail the potential interactions and synergies between conventional antidepressants and natural mood enhancers like St. John’s Wort and SAM-e.'
        },
        {
            "title": "Bone Health: Supplements & Medications",
            "prompt": 'Discuss the combined effects of osteoporosis medications and natural supplements like calcium, vitamin D, and red clover on bone health.'
        },
        {
            "title": "Heart Health: Statins & Herbal Supplements",
            "prompt": 'Analyze the potential interactions between statin medications and herbal supplements like red yeast rice and coenzyme Q10 in managing cholesterol levels.'
        },
        {
            "title": "Liver Function: Medications & Detoxifying Herbs",
            "prompt": 'How do conventional medications processed by the liver interact with detoxifying herbs like dandelion root and milk thistle?'
        },
        {
            "title": "Digestive Health: IBS Medications & Probiotics",
            "prompt": 'Explain the potential synergies and conflicts between medications for irritable bowel syndrome (IBS) and natural remedies like probiotics and peppermint oil.'
        },
        {
            "title": "Respiratory Health: Asthma Medications & Herbal Teas",
            "prompt": 'Discuss the implications of using asthma medications alongside herbal teas like mullein and licorice root.'
        },
        {
            "title": "Neurological Health: Alzheimer's Medications & Natural Nootropics",
            "prompt": 'Detail the potential interactions between Alzheimer’s disease medications and natural nootropics like ginkgo biloba and lion’s mane mushroom.'
        },
        {
            "title": "Skin Health: Acne Medications & Herbal Topicals",
            "prompt": 'Analyze the combined effects of conventional acne medications and herbal topicals like tea tree oil and witch hazel.'
        },
        {
            "title": "Pain Management: NSAIDs & Natural Anti-inflammatories",
            "prompt": 'Discuss the potential synergies and conflicts between NSAIDs and natural anti-inflammatories like turmeric and ginger.'
        },
        {
            "title": "Thyroid Health: Thyroid Medications & Natural Supplements",
            "prompt": 'How do thyroid medications interact with natural supplements like ashwagandha and bladderwrack?'
        },
        {
            "title": "Eye Health: Glaucoma Medications & Herbal Remedies",
            "prompt": 'Explain the implications of using glaucoma medications alongside herbal remedies like bilberry and eyebright.'
        },
        {
            "title": "Joint Health: Arthritis Medications & Natural Anti-inflammatories",
            "prompt": 'Detail the potential interactions between arthritis medications and natural anti-inflammatories like boswellia and devil’s claw.'
        },
        {
            "title": "Mental Health: ADHD Medications & Natural Calmatives",
            "prompt": 'Discuss the potential synergies and conflicts between ADHD medications and natural calmatives like lemon balm and passionflower.'
        },
        {
            "title": "Immune Health: Immunosuppressants & Immune-Boosting Herbs",
            "prompt": 'How do immunosuppressant drugs interact with immune-boosting herbs like echinacea and astragalus?'
        },
        {
            "title": "Reproductive Health: Birth Control & Herbal Remedies",
            "prompt": 'Explain the implications of using birth control alongside herbal remedies like chasteberry and black cohosh.'
        },
        {
            "title": "Sleep Disorders: Sleep Medications & Natural Sedatives",
            "prompt": 'Detail the potential interactions between sleep medications and natural sedatives like valerian root and chamomile.'
        },
        {
            "title": "Cardiovascular Health: Blood Thinners & Herbal Supplements",
            "prompt": 'Analyze the potential interactions between blood thinners and herbal supplements like ginkgo biloba and dong quai.'
        }
    ]


    for rp in role_plays:
        with st.expander(rp["title"]):
            st.write(rp["prompt"])

