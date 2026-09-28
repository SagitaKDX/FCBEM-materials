
---

# Appendix A. Discourse coding scheme

Examples are quoted verbatim from the corpus in Vietnamese, with English glosses. Original spelling and abbreviation are preserved. Appendices are not counted toward the word limit.

**Table A1. Coding scheme for the four constructs**

| Construct | Discourse indicator | Vietnamese example | English gloss |
| :--- | :--- | :--- | :--- |
| `R_uncanny` | **Local**: names a particular feature of body, motion, or voice as wrong, artificial, or unsettling. | *"Mắt trái hơi lỗi nha bác Nhân ơi"* | "The left eye is a bit glitched, Nhân" |
| | | *"Cái vai cứ rung rung giật giật nhìn nó cứ cringe thế nào ấy"* | "The shoulder keeps twitching, it looks cringe somehow" |
| | | *"Sao giọng ko thống nhất"* | "Why isn't the voice consistent" |
| `R_ai_skepticism` | **General**: frames artificiality itself as a problem — deception, engagement-baiting, inauthenticity — without citing a specific feature. | *"AI thì vẫn là AI k thể giống ng thường dc"* | "AI is still AI, it can never be like a normal person" |
| | | *"AI không thực, sao không quay trực tiếp"* | "AI isn't real, why not film it live" |
| `S_parasocial` | Treats the figure as a **person**: familiar address, questions about private life, requests for content, defence against criticism. | *"Em lúc nào cũng xinh đẹp và dễ thương như vậy"* | "You're always this pretty and sweet" |
| | | *"chị hok già đâu…chị rất đẹp lại kon giỏi nữa"* | "You're not old at all… you're beautiful and talented too" |
| | *Defence sub-type* (see Rule 2) | *"Nghĩ sao ẻm là AI nhỉ?"* | "What makes you think she's AI?" |
| `C_commercial` | Orients toward the character's **goods**: price, purchase link, shipping, or stated intent to buy. | *"Bán gì em mua cho chị ơi"* | "What are you selling, I'll buy it" |
| | | *"Em ơi cho chị hỏi mẫu bộ này em mua ở đâu ạ"* | "Where did you buy this outfit?" |

A comment may carry several constructs. One citing a specific flaw *and* objecting to AI use in general receives both `R_uncanny` and `R_ai_skepticism`.

**Table A2. Aspects and polarity**

| Aspect | Scope | Vietnamese example (+1) | English gloss |
| :--- | :--- | :--- | :--- |
| `asp_appearance` | Face, skin, figure, clothing, 3D realism | *"em dễ thương quá"* | "you're so cute" |
| `asp_voice_motion` | Voice, lip-sync, movement, facial expression | *"AI hát cỡ này thì ng hát sao so đc"* | "if AI sings like this, how can human singers compete" |
| `asp_ai_nature` | Being an AI character; the technology; AI ethics | *"Thời buổi AI đẹp hơn đồ thật"* | "these days AI looks better than the real thing" |
| `asp_persona` | Personality, humour, charm, manner of speaking | *"Phải cứng thế chứ em nhỉ!"* | "that's the way to stand firm, right!" |

Polarity is coded `+1` (praise), `0` (mentioned, neutral), `−1` (criticism), or `NA` (not mentioned). `NA` is distinguished from `0`, and the denominator of every aspect rate counts only mentioning comments. A fifth aspect, `asp_product_brand`, appears in the codebook but is excluded from results (Precision = Recall = 0 on the gold set).

## Two disambiguation rules specific to Vietnamese

**Rule 1 — lowercase *ai* is a pronoun, not the technology.** In Vietnamese, *ai* means *who*. A case-insensitive keyword filter therefore counts phrases such as *"Ai mua khô bò hôm"* ("who's buying dried beef today") and *"thì nó là ai mà bạn"* ("well, who is she then") as references to artificial intelligence. Applied to this corpus, such a filter inflates AI-mention rates by a factor of 1.4 to 2.3. Only capitalised *AI*, or explicit phrases — *trí tuệ nhân tạo*, *nhân vật ảo*, *deepfake* — count as references to the technology.

**Rule 2 — defending the character against AI criticism is `S_parasocial`, not `R_ai_skepticism`.** Comments such as *"Tiểu My này có thật ngoài đời nhé mình gặp rồi"* ("this Tiểu My is real, I've met her") or *"Ảo cũng yêu Mỹ luôn"* ("virtual or not, I still love Mỹ") mention AI but argue *for* the character. Coding them as scepticism would make resistance appear to rise at precisely the moments engagement is strongest. These receive `S_parasocial = 1`, `R_ai_skepticism = 0`, and `asp_ai_nature = +1`.

A related boundary: praise of the technology is not scepticism. *"AI giờ ghê thật"* ("AI is impressive these days") is coded `asp_ai_nature = +1` with `R_ai_skepticism = 0`.
