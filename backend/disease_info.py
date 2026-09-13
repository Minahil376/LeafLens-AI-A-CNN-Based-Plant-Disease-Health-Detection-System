from dataclasses import dataclass, field


@dataclass
class DiseaseEntry:
    class_index: int
    raw_class_name: str
    class_label: str
    plant_name: str
    disease_name: str
    is_healthy: bool
    description: str
    treatment: list


DISEASE_INFO: dict = {
    0: DiseaseEntry(
        class_index=0,
        raw_class_name="Apple___Apple_scab",
        class_label="Apple — Apple Scab",
        plant_name="Apple",
        disease_name="Apple Scab",
        is_healthy=False,
        description=(
            "Apple scab is a common fungal disease caused by Venturia inaequalis that affects "
            "leaves, blossoms, and fruit. Infected leaves develop olive-green to dark brown velvety "
            "spots, and severely infected leaves may drop early. Fruit develops scab-like lesions "
            "that can crack, making it unmarketable."
        ),
        treatment=[
            "Apply fungicides (captan, myclobutanil, or mancozeb) starting at bud break and repeating every 7–14 days.",
            "Remove and destroy fallen infected leaves to reduce overwintering spore populations.",
            "Plant resistant apple varieties such as Liberty, Freedom, or Enterprise.",
            "Prune trees to improve air circulation and reduce humidity within the canopy.",
        ],
    ),
    1: DiseaseEntry(
        class_index=1,
        raw_class_name="Apple___Black_rot",
        class_label="Apple — Black Rot",
        plant_name="Apple",
        disease_name="Black Rot",
        is_healthy=False,
        description=(
            "Black rot is a fungal disease caused by Botryosphaeria obtusa that infects apple "
            "leaves, fruit, and bark. Leaf symptoms appear as purple spots that enlarge and turn "
            "brown with a 'frog-eye' appearance. Fruit rot begins at the calyx end and progresses "
            "until the entire fruit turns black and mummified."
        ),
        treatment=[
            "Prune out and destroy all dead or diseased wood, including mummified fruit, during dormancy.",
            "Apply fungicides such as captan or thiophanate-methyl from pink bud stage through harvest.",
            "Remove cankers by cutting 15 cm below the margin of visible infection.",
            "Maintain tree vigor through proper fertilization and irrigation to improve natural resistance.",
        ],
    ),
    2: DiseaseEntry(
        class_index=2,
        raw_class_name="Apple___Cedar_apple_rust",
        class_label="Apple — Cedar Apple Rust",
        plant_name="Apple",
        disease_name="Cedar Apple Rust",
        is_healthy=False,
        description=(
            "Cedar apple rust is a fungal disease caused by Gymnosporangium juniperi-virginianae "
            "that requires both apple and eastern red cedar trees to complete its life cycle. "
            "Bright orange-yellow spots appear on upper leaf surfaces in spring, and tube-like "
            "lesions develop on the undersides of infected leaves and fruit."
        ),
        treatment=[
            "Apply protective fungicides (myclobutanil, triadimefon) from pink bud stage through 3–4 weeks after petal fall.",
            "Remove nearby eastern red cedar or juniper trees if practical to break the disease cycle.",
            "Plant rust-resistant apple varieties such as Liberty, Redfree, or Pristine.",
            "Inspect and remove cedar-apple rust galls from nearby junipers before they produce spores in spring.",
        ],
    ),
    3: DiseaseEntry(
        class_index=3,
        raw_class_name="Apple___healthy",
        class_label="Apple — Healthy",
        plant_name="Apple",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The apple plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves show normal green coloration, proper size, and no lesions, spots, or abnormal "
            "discoloration. Continue regular monitoring and good cultural practices."
        ),
        treatment=[],
    ),
    4: DiseaseEntry(
        class_index=4,
        raw_class_name="Blueberry___healthy",
        class_label="Blueberry — Healthy",
        plant_name="Blueberry",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The blueberry plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves display normal coloration and structure. Continue regular monitoring and "
            "maintain good cultural practices including proper soil pH and adequate irrigation."
        ),
        treatment=[],
    ),
    5: DiseaseEntry(
        class_index=5,
        raw_class_name="Cherry_(including_sour)___Powdery_mildew",
        class_label="Cherry — Powdery Mildew",
        plant_name="Cherry",
        disease_name="Powdery Mildew",
        is_healthy=False,
        description=(
            "Powdery mildew on cherry is caused by Podosphaera clandestina and appears as white, "
            "powdery fungal growth on young leaves, shoots, and fruit. Infected leaves may curl, "
            "distort, and drop prematurely. Severe infections reduce photosynthesis and fruit "
            "quality, and can cause significant yield losses in susceptible varieties."
        ),
        treatment=[
            "Apply sulfur-based or potassium bicarbonate fungicides at first sign of disease.",
            "Use sterol-inhibiting fungicides (myclobutanil, trifloxystrobin) for systemic control.",
            "Prune to improve air circulation and reduce humidity within the tree canopy.",
            "Avoid excessive nitrogen fertilization which promotes susceptible succulent growth.",
        ],
    ),
    6: DiseaseEntry(
        class_index=6,
        raw_class_name="Cherry_(including_sour)___healthy",
        class_label="Cherry — Healthy",
        plant_name="Cherry",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The cherry plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves show normal deep-green coloration and glossy surface without spots, lesions, "
            "or powdery coatings. Continue regular monitoring and good orchard management practices."
        ),
        treatment=[],
    ),
    7: DiseaseEntry(
        class_index=7,
        raw_class_name="Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
        class_label="Corn — Gray Leaf Spot (Cercospora)",
        plant_name="Corn",
        disease_name="Gray Leaf Spot (Cercospora)",
        is_healthy=False,
        description=(
            "Gray leaf spot, caused by Cercospora zeae-maydis, is one of the most significant "
            "foliar diseases of corn worldwide. Lesions begin as small, tan-colored spots with "
            "yellow halos that elongate into rectangular, gray to brown lesions running parallel "
            "to leaf veins. Severe infections cause premature leaf death and significant yield loss."
        ),
        treatment=[
            "Plant resistant hybrid corn varieties rated for gray leaf spot tolerance.",
            "Apply foliar fungicides (strobilurins, triazoles) at VT to R1 growth stage when disease pressure is high.",
            "Practice crop rotation with non-host crops such as soybean or wheat to reduce inoculum.",
            "Reduce crop residue through tillage to limit overwintering of the pathogen.",
        ],
    ),
    8: DiseaseEntry(
        class_index=8,
        raw_class_name="Corn_(maize)___Common_rust_",
        class_label="Corn — Common Rust",
        plant_name="Corn",
        disease_name="Common Rust",
        is_healthy=False,
        description=(
            "Common rust of corn is caused by Puccinia sorghi and is characterized by small, "
            "circular to elongate cinnamon-brown pustules scattered on both upper and lower leaf "
            "surfaces. As the disease progresses, pustules may turn dark brown to black. Severely "
            "infected plants show reduced photosynthetic capacity and potential yield reductions."
        ),
        treatment=[
            "Plant resistant corn hybrids, which is the most effective management strategy.",
            "Apply fungicides (propiconazole, azoxystrobin) when rust is first detected and conditions favor disease.",
            "Monitor fields regularly starting from early vegetative stages in high-risk areas.",
            "Avoid late planting dates that expose plants to higher rust pressure during grain fill.",
        ],
    ),
    9: DiseaseEntry(
        class_index=9,
        raw_class_name="Corn_(maize)___Northern_Leaf_Blight",
        class_label="Corn — Northern Leaf Blight",
        plant_name="Corn",
        disease_name="Northern Leaf Blight",
        is_healthy=False,
        description=(
            "Northern leaf blight, caused by Exserohilum turcicum, produces characteristic long "
            "cigar-shaped, grayish-green to tan lesions up to 15 cm long on corn leaves. The disease "
            "typically appears first on lower leaves and progresses upward. Under humid conditions, "
            "grayish-black sporulation is visible within lesions, and severe infection before "
            "tasseling can cause significant yield loss."
        ),
        treatment=[
            "Plant resistant corn hybrids with Ht gene resistance or partial resistance.",
            "Apply foliar fungicides (azoxystrobin, propiconazole) when lesions first appear on lower leaves.",
            "Practice crop rotation and manage crop residue to reduce inoculum carryover.",
            "Ensure adequate plant spacing for good air circulation within the canopy.",
        ],
    ),
    10: DiseaseEntry(
        class_index=10,
        raw_class_name="Corn_(maize)___healthy",
        class_label="Corn — Healthy",
        plant_name="Corn",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The corn plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves display uniform green coloration without lesions, pustules, or abnormal spotting. "
            "Continue regular scouting and maintain proper agronomic practices throughout the season."
        ),
        treatment=[],
    ),
    11: DiseaseEntry(
        class_index=11,
        raw_class_name="Grape___Black_rot",
        class_label="Grape — Black Rot",
        plant_name="Grape",
        disease_name="Black Rot",
        is_healthy=False,
        description=(
            "Black rot, caused by Guignardia bidwellii, is a destructive fungal disease of grapes "
            "that can destroy the entire crop if left unmanaged. Small reddish-brown circular spots "
            "appear on leaves, and infected berries turn brown and shrivel into hard, black, wrinkled "
            "mummies. The fungus overwinters in mummified fruit and infected canes."
        ),
        treatment=[
            "Apply fungicides (mancozeb, myclobutanil, or captan) starting at bud break and continuing through bloom.",
            "Remove and destroy all mummified berries and infected canes during winter pruning.",
            "Ensure good air circulation through proper vine training and canopy management.",
            "Time fungicide applications to protect during the critical period from shoot emergence to two to three weeks after bloom.",
        ],
    ),
    12: DiseaseEntry(
        class_index=12,
        raw_class_name="Grape___Esca_(Black_Measles)",
        class_label="Grape — Esca (Black Measles)",
        plant_name="Grape",
        disease_name="Esca (Black Measles)",
        is_healthy=False,
        description=(
            "Esca, also known as black measles, is a complex grapevine trunk disease caused by "
            "a combination of wood-rotting fungi including Phaeomoniella chlamydospora and Phaeoacremonium "
            "species. Symptoms include tiger-stripe leaf patterns, berry spotting, and internal wood "
            "discoloration. Severely affected vines may show sudden vine death (apoplexy) during hot weather."
        ),
        treatment=[
            "Remove and destroy infected wood by pruning below the visible discoloration.",
            "Apply wound sealants containing fungicide (thiophanate-methyl) after pruning to protect wounds.",
            "Avoid large pruning wounds; delay pruning until late in the dormant season to reduce infection.",
            "Replace severely affected vines; there is no cure for established trunk infections.",
        ],
    ),
    13: DiseaseEntry(
        class_index=13,
        raw_class_name="Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
        class_label="Grape — Leaf Blight (Isariopsis)",
        plant_name="Grape",
        disease_name="Leaf Blight (Isariopsis)",
        is_healthy=False,
        description=(
            "Grape leaf blight caused by Isariopsis clavispora (Cladosporium viticola) produces "
            "irregular brown to reddish-brown lesions on leaf surfaces. The lesions may coalesce "
            "causing large areas of tissue death. Severely infected leaves drop prematurely, "
            "weakening the vine and reducing fruit quality and overall vigor."
        ),
        treatment=[
            "Apply copper-based or mancozeb fungicides when symptoms first appear.",
            "Improve canopy ventilation through proper training and leaf removal around the fruit zone.",
            "Remove and destroy infected plant debris at the end of the season.",
            "Avoid overhead irrigation which promotes leaf wetness and disease spread.",
        ],
    ),
    14: DiseaseEntry(
        class_index=14,
        raw_class_name="Grape___healthy",
        class_label="Grape — Healthy",
        plant_name="Grape",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The grapevine appears healthy with no visible signs of disease or pest damage. "
            "Leaves display normal green coloration without spots, lesions, or discoloration. "
            "Continue regular monitoring and maintain good viticultural practices."
        ),
        treatment=[],
    ),
    15: DiseaseEntry(
        class_index=15,
        raw_class_name="Orange___Haunglongbing_(Citrus_greening)",
        class_label="Orange — Huanglongbing (Citrus Greening)",
        plant_name="Orange",
        disease_name="Huanglongbing (Citrus Greening)",
        is_healthy=False,
        description=(
            "Huanglongbing (HLB), or citrus greening, is considered the most serious citrus disease "
            "in the world, caused by the bacterium Candidatus Liberibacter asiaticus transmitted by "
            "the Asian citrus psyllid. Infected trees show blotchy mottle on leaves (asymmetric "
            "yellowing), stunted growth, and produce small, misshapen, bitter fruit that remain "
            "partially green. There is currently no cure for infected trees."
        ),
        treatment=[
            "Control Asian citrus psyllid populations using systemic insecticides (imidacloprid, thiamethoxam).",
            "Remove and destroy infected trees promptly to reduce the inoculum source.",
            "Plant certified disease-free nursery stock from reputable suppliers.",
            "Apply nutritional sprays and micronutrients to extend the productive life of mildly symptomatic trees.",
        ],
    ),
    16: DiseaseEntry(
        class_index=16,
        raw_class_name="Peach___Bacterial_spot",
        class_label="Peach — Bacterial Spot",
        plant_name="Peach",
        disease_name="Bacterial Spot",
        is_healthy=False,
        description=(
            "Bacterial spot of peach is caused by Xanthomonas arboricola pv. pruni and affects "
            "leaves, fruit, and twigs. Leaf symptoms include small, water-soaked spots that turn "
            "purple to brown and often fall out leaving a shot-hole appearance. Fruit lesions "
            "are superficial but create entry points for secondary rots, severely reducing marketability."
        ),
        treatment=[
            "Apply copper-based bactericides starting at shuck-split and continuing through summer.",
            "Plant resistant peach varieties where available for your region.",
            "Prune infected twigs during dry weather and disinfect pruning tools between cuts.",
            "Avoid overhead irrigation; use drip irrigation to reduce leaf wetness duration.",
        ],
    ),
    17: DiseaseEntry(
        class_index=17,
        raw_class_name="Peach___healthy",
        class_label="Peach — Healthy",
        plant_name="Peach",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The peach tree appears healthy with no visible signs of disease or pest damage. "
            "Leaves show normal green coloration without spots, shot-holes, or discoloration. "
            "Continue regular monitoring and good orchard management practices."
        ),
        treatment=[],
    ),
    18: DiseaseEntry(
        class_index=18,
        raw_class_name="Pepper,_bell___Bacterial_spot",
        class_label="Bell Pepper — Bacterial Spot",
        plant_name="Bell Pepper",
        disease_name="Bacterial Spot",
        is_healthy=False,
        description=(
            "Bacterial spot of bell pepper is caused by Xanthomonas euvesicatoria and is one of the "
            "most destructive diseases of peppers in warm, wet climates. Water-soaked lesions appear "
            "on leaves, stems, and fruit that turn brown and necrotic. Defoliation exposes fruit to "
            "sunscald and severely reduces yield. The pathogen spreads rapidly through rain splash "
            "and contaminated seed."
        ),
        treatment=[
            "Apply copper-based bactericides preventatively starting from transplant and repeating every 5–7 days during wet weather.",
            "Use certified disease-free transplants and seed treated with hot water or copper sulfate.",
            "Practice crop rotation of 2–3 years with non-solanaceous crops.",
            "Avoid overhead irrigation and working in fields when foliage is wet.",
        ],
    ),
    19: DiseaseEntry(
        class_index=19,
        raw_class_name="Pepper,_bell___healthy",
        class_label="Bell Pepper — Healthy",
        plant_name="Bell Pepper",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The bell pepper plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves show deep green coloration without spots, lesions, or yellowing. Continue "
            "regular monitoring and maintain good cultural practices."
        ),
        treatment=[],
    ),
    20: DiseaseEntry(
        class_index=20,
        raw_class_name="Potato___Early_blight",
        class_label="Potato — Early Blight",
        plant_name="Potato",
        disease_name="Early Blight",
        is_healthy=False,
        description=(
            "Early blight of potato is caused by Alternaria solani and primarily affects older, "
            "lower leaves first. Characteristic symptoms include dark brown to black circular lesions "
            "with concentric rings forming a bull's-eye or target pattern, often surrounded by a "
            "yellow halo. Severe defoliation reduces tuber size and yield, and infected tubers may "
            "develop dark, slightly sunken lesions on their surface."
        ),
        treatment=[
            "Apply fungicides (chlorothalonil, mancozeb, azoxystrobin) preventatively starting when plants reach 15–20 cm height.",
            "Remove and destroy infected lower leaves to slow disease progression.",
            "Maintain adequate soil fertility, particularly nitrogen, to keep plants vigorous.",
            "Use certified disease-free seed potatoes and practice crop rotation with non-solanaceous crops.",
        ],
    ),
    21: DiseaseEntry(
        class_index=21,
        raw_class_name="Potato___Late_blight",
        class_label="Potato — Late Blight",
        plant_name="Potato",
        disease_name="Late Blight",
        is_healthy=False,
        description=(
            "Late blight, caused by the oomycete Phytophthora infestans, is the most historically "
            "significant potato disease and was responsible for the Irish Famine. Water-soaked, "
            "pale green to brown lesions appear on leaves and can expand rapidly under cool, moist "
            "conditions. A white mold is visible on the underside of infected leaves. The pathogen "
            "can destroy an entire field within days under favorable conditions."
        ),
        treatment=[
            "Apply fungicides (mancozeb, chlorothalonil, cymoxanil) preventatively before disease onset, especially during cool, wet weather.",
            "Use late-blight-resistant potato varieties such as Defender, Jacqueline Lee, or Mountain Supreme.",
            "Destroy infected plant material and volunteer potato plants to reduce inoculum.",
            "Hill soil around potato plants to protect tubers from spores washing down into the soil.",
        ],
    ),
    22: DiseaseEntry(
        class_index=22,
        raw_class_name="Potato___healthy",
        class_label="Potato — Healthy",
        plant_name="Potato",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The potato plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves are uniformly green without lesions, spots, or abnormal discoloration. Continue "
            "regular monitoring and maintain good agronomic practices."
        ),
        treatment=[],
    ),
    23: DiseaseEntry(
        class_index=23,
        raw_class_name="Raspberry___healthy",
        class_label="Raspberry — Healthy",
        plant_name="Raspberry",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The raspberry plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves display normal green coloration without spots, mold, or discoloration. Continue "
            "regular monitoring and maintain good cultural practices."
        ),
        treatment=[],
    ),
    24: DiseaseEntry(
        class_index=24,
        raw_class_name="Soybean___healthy",
        class_label="Soybean — Healthy",
        plant_name="Soybean",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The soybean plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves show normal trifoliate structure with uniform green coloration and no abnormal "
            "spotting or discoloration. Continue regular scouting and good agronomic practices."
        ),
        treatment=[],
    ),
    25: DiseaseEntry(
        class_index=25,
        raw_class_name="Squash___Powdery_mildew",
        class_label="Squash — Powdery Mildew",
        plant_name="Squash",
        disease_name="Powdery Mildew",
        is_healthy=False,
        description=(
            "Powdery mildew on squash is caused by Podosphaera xanthii and Erysiphe cichoracearum. "
            "It appears as white to gray powdery fungal growth on the surface of leaves, stems, and "
            "petioles. Unlike most fungal diseases, it thrives in warm, dry conditions with high "
            "relative humidity. Severe infections reduce plant vigor, cause premature leaf death, "
            "and decrease fruit quality and yield."
        ),
        treatment=[
            "Apply fungicides (potassium bicarbonate, sulfur, neem oil, or myclobutanil) at first sign of infection.",
            "Remove severely infected leaves to reduce spore load and improve air circulation.",
            "Plant resistant squash varieties when available.",
            "Avoid overhead irrigation and water stress which can increase susceptibility.",
        ],
    ),
    26: DiseaseEntry(
        class_index=26,
        raw_class_name="Strawberry___Leaf_scorch",
        class_label="Strawberry — Leaf Scorch",
        plant_name="Strawberry",
        disease_name="Leaf Scorch",
        is_healthy=False,
        description=(
            "Strawberry leaf scorch is caused by Diplocarpon earlianum and is one of the most "
            "common foliar diseases of strawberries. Small, irregular purple to dark brown spots "
            "appear on the upper leaf surface. As lesions enlarge and coalesce, the leaf appears "
            "scorched. Severely infected plants lose leaves prematurely, reducing plant vigor, "
            "runner production, and fruit yield over multiple seasons."
        ),
        treatment=[
            "Apply fungicides (captan, myclobutanil, or thiram) beginning in early spring and after renovation.",
            "Remove old, infected leaves during renovation immediately after harvest.",
            "Plant certified disease-free transplants; use resistant varieties where available.",
            "Improve air circulation by proper plant spacing and avoid excessive nitrogen application.",
        ],
    ),
    27: DiseaseEntry(
        class_index=27,
        raw_class_name="Strawberry___healthy",
        class_label="Strawberry — Healthy",
        plant_name="Strawberry",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The strawberry plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves show normal green coloration without spots, lesions, or purpling. Continue "
            "regular monitoring and good cultural practices including proper renovation after harvest."
        ),
        treatment=[],
    ),
    28: DiseaseEntry(
        class_index=28,
        raw_class_name="Tomato___Bacterial_spot",
        class_label="Tomato — Bacterial Spot",
        plant_name="Tomato",
        disease_name="Bacterial Spot",
        is_healthy=False,
        description=(
            "Bacterial spot of tomato is caused by Xanthomonas species and affects all above-ground "
            "parts of the plant. Small, water-soaked spots appear on leaves that turn brown to black "
            "with yellow halos, giving a shot-hole appearance when centers fall out. Fruit lesions "
            "start as small, raised spots that become dark and scab-like. The disease spreads rapidly "
            "in warm, wet weather and through infected transplants."
        ),
        treatment=[
            "Apply copper-based bactericides preventatively, rotating with mancozeb for resistance management.",
            "Use certified disease-free or pathogen-tested seed and transplants.",
            "Practice crop rotation and avoid working in fields when foliage is wet.",
            "Remove and destroy severely infected plant material to reduce inoculum sources.",
        ],
    ),
    29: DiseaseEntry(
        class_index=29,
        raw_class_name="Tomato___Early_blight",
        class_label="Tomato — Early Blight",
        plant_name="Tomato",
        disease_name="Early Blight",
        is_healthy=False,
        description=(
            "Early blight of tomato, caused by Alternaria solani, is one of the most common "
            "tomato diseases worldwide. Symptoms first appear on older, lower leaves as dark brown "
            "circular spots with concentric rings forming a characteristic bull's-eye or target "
            "pattern. Yellow tissue often surrounds the lesions. Stems may develop dark, sunken "
            "lesions at soil level (collar rot), and fruit can be affected near the stem attachment."
        ),
        treatment=[
            "Apply fungicides (chlorothalonil, mancozeb, azoxystrobin) preventatively before disease onset.",
            "Remove and destroy lower infected leaves as soon as symptoms appear.",
            "Stake and mulch plants to improve air circulation and reduce soil splash onto leaves.",
            "Rotate crops with non-solanaceous plants for at least two to three years.",
        ],
    ),
    30: DiseaseEntry(
        class_index=30,
        raw_class_name="Tomato___Late_blight",
        class_label="Tomato — Late Blight",
        plant_name="Tomato",
        disease_name="Late Blight",
        is_healthy=False,
        description=(
            "Late blight, caused by Phytophthora infestans, is one of the most destructive tomato "
            "diseases and can destroy entire plantings within days under favorable cool, moist "
            "conditions. Large, irregular, water-soaked lesions appear on leaves and turn dark brown "
            "to black. White mold may be visible on the underside of infected leaves. Fruit develops "
            "greasy, brown lesions. The pathogen spreads rapidly through airborne spores."
        ),
        treatment=[
            "Apply fungicides (mancozeb, chlorothalonil, cymoxanil, or fluopicolide) at first sign of disease or during high-risk weather.",
            "Remove and destroy infected plants immediately to prevent spread.",
            "Avoid overhead irrigation and wetting foliage; water at the base of plants.",
            "Monitor weather forecasts and apply preventative sprays during cool, wet periods.",
        ],
    ),
    31: DiseaseEntry(
        class_index=31,
        raw_class_name="Tomato___Leaf_Mold",
        class_label="Tomato — Leaf Mold",
        plant_name="Tomato",
        disease_name="Leaf Mold",
        is_healthy=False,
        description=(
            "Tomato leaf mold is caused by Passalora fulva (formerly Cladosporium fulvum) and "
            "primarily affects greenhouse-grown tomatoes, though it can also occur in the field. "
            "Pale green to yellow patches appear on upper leaf surfaces, with olive-green to gray "
            "velvety fungal growth on the corresponding lower surfaces. Severely infected leaves "
            "curl, wither, and drop, reducing yield and fruit quality."
        ),
        treatment=[
            "Reduce humidity in greenhouses by improving ventilation and spacing plants adequately.",
            "Apply fungicides (mancozeb, chlorothalonil, copper-based products) when disease first appears.",
            "Use resistant tomato varieties with Cf genes for resistance to leaf mold races.",
            "Remove and destroy infected leaves to reduce spore production and spread.",
        ],
    ),
    32: DiseaseEntry(
        class_index=32,
        raw_class_name="Tomato___Septoria_leaf_spot",
        class_label="Tomato — Septoria Leaf Spot",
        plant_name="Tomato",
        disease_name="Septoria Leaf Spot",
        is_healthy=False,
        description=(
            "Septoria leaf spot, caused by Septoria lycopersici, is one of the most common tomato "
            "foliar diseases in humid regions. Symptoms first appear on lower, older leaves as "
            "numerous small, circular spots with dark brown margins and lighter gray centers, often "
            "containing dark specks (pycnidia). As disease progresses upward, defoliation weakens "
            "the plant and exposes fruit to sunscald, reducing overall yield."
        ),
        treatment=[
            "Apply fungicides (chlorothalonil, mancozeb, copper-based products) starting when plants first flower.",
            "Remove and destroy infected lower leaves to slow upward disease progression.",
            "Stake plants and mulch soil to reduce splash dispersal of spores.",
            "Practice crop rotation of at least three years and avoid working in wet fields.",
        ],
    ),
    33: DiseaseEntry(
        class_index=33,
        raw_class_name="Tomato___Spider_mites Two-spotted_spider_mite",
        class_label="Tomato — Spider Mites",
        plant_name="Tomato",
        disease_name="Spider Mites",
        is_healthy=False,
        description=(
            "Two-spotted spider mite (Tetranychus urticae) is a common pest of tomatoes that causes "
            "significant damage, particularly during hot, dry conditions. Infested leaves show fine "
            "stippling or bronzing on the upper surface due to mite feeding, and may develop fine "
            "webbing on the undersides. Severe infestations cause leaf yellowing, premature drop, "
            "and significant yield reduction. Mites reproduce rapidly, with populations exploding "
            "in hot, dusty conditions."
        ),
        treatment=[
            "Apply miticides (abamectin, bifenazate, spiromesifen) when mite populations exceed threshold levels.",
            "Use predatory mites (Phytoseiulus persimilis) as biological control in greenhouse settings.",
            "Ensure adequate irrigation as water-stressed plants are more susceptible to mite infestations.",
            "Remove and destroy heavily infested plant material; use strong water sprays to dislodge mites from leaves.",
        ],
    ),
    34: DiseaseEntry(
        class_index=34,
        raw_class_name="Tomato___Target_Spot",
        class_label="Tomato — Target Spot",
        plant_name="Tomato",
        disease_name="Target Spot",
        is_healthy=False,
        description=(
            "Target spot of tomato is caused by Corynespora cassiicola and produces circular to "
            "irregular brown lesions with concentric rings giving a target-like appearance on "
            "leaves, stems, and fruit. The disease can affect all above-ground plant parts and "
            "is most severe in warm, humid conditions. Defoliation from severe infections reduces "
            "fruit yield and exposes fruit to direct sunlight damage."
        ),
        treatment=[
            "Apply fungicides (chlorothalonil, mancozeb, azoxystrobin) preventatively or at first sign of disease.",
            "Maintain good air circulation through staking, pruning suckers, and proper plant spacing.",
            "Avoid wetting foliage with overhead irrigation; use drip or furrow irrigation instead.",
            "Practice crop rotation with non-solanaceous crops for at least two years.",
        ],
    ),
    35: DiseaseEntry(
        class_index=35,
        raw_class_name="Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        class_label="Tomato — Yellow Leaf Curl Virus",
        plant_name="Tomato",
        disease_name="Yellow Leaf Curl Virus",
        is_healthy=False,
        description=(
            "Tomato yellow leaf curl virus (TYLCV) is a begomovirus transmitted by the silverleaf "
            "whitefly (Bemisia tabaci). Infected plants show severe upward curling and yellowing of "
            "young leaves, stunted growth, and greatly reduced fruit set. The virus can cause nearly "
            "complete crop loss when infection occurs early in the season. There is no cure once a "
            "plant is infected, making prevention and vector control essential."
        ),
        treatment=[
            "Control whitefly populations using systemic insecticides (imidacloprid, thiamethoxam) or insect-growth regulators.",
            "Use reflective mulches to repel whiteflies and slow virus spread in the field.",
            "Plant TYLCV-resistant or tolerant tomato varieties when available.",
            "Remove and destroy infected plants promptly to reduce the virus source for whitefly transmission.",
        ],
    ),
    36: DiseaseEntry(
        class_index=36,
        raw_class_name="Tomato___Tomato_mosaic_virus",
        class_label="Tomato — Mosaic Virus",
        plant_name="Tomato",
        disease_name="Mosaic Virus",
        is_healthy=False,
        description=(
            "Tomato mosaic virus (ToMV) and related tobamovirus tomato mosaic virus (TMV) cause "
            "mottled yellow-green mosaic patterns on leaves, leaf distortion, and stunted growth. "
            "Infected plants produce fewer and smaller fruit. The virus is extremely stable and "
            "spreads through mechanical contact, contaminated tools, soil, and infected seed. "
            "It can persist in dry plant debris for years, making sanitation critical."
        ),
        treatment=[
            "Use certified virus-free, resistant tomato varieties (with Tm-2 or Tm-2² resistance genes).",
            "Disinfect all tools and equipment with bleach solution or trisodium phosphate before use.",
            "Wash hands thoroughly before handling plants, especially after using tobacco products.",
            "Remove and destroy infected plants immediately; avoid replanting tomatoes in the same soil for several years.",
        ],
    ),
    37: DiseaseEntry(
        class_index=37,
        raw_class_name="Tomato___healthy",
        class_label="Tomato — Healthy",
        plant_name="Tomato",
        disease_name="Healthy",
        is_healthy=True,
        description=(
            "The tomato plant appears healthy with no visible signs of disease or pest damage. "
            "Leaves show uniform deep-green coloration without spots, lesions, mosaic patterns, "
            "or abnormal curling. Continue regular monitoring and maintain good cultural practices "
            "including adequate staking, irrigation, and fertilization."
        ),
        treatment=[],
    ),
}

assert len(DISEASE_INFO) == 38, f"Expected 38 disease entries, got {len(DISEASE_INFO)}"
