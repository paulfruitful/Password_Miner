import itertools
greek='αβγδϵζηθικλμνξοπρστυϕχψω'
physics= ''.join(set('θφθφîĵk̂θφr̂θ̂φ̂ρφzρ̂φ̂,ẑn̂t̂hℓτfω'))
japanese=''.join(set('ぁ あ ぅ た て な に ぬ の は る ゑ ゖ ん ゟ ァ ス ダ デ ト ナ ニ ハ ピ ビ プ ブ ベ デ ホ ボ ム モ ㍿ じ す ず だ ぎ む み ゅ ゟ ネ'))
chinese=''.join(set('山 人 口 刀 木 日 女 子 目 水 三 鳥 馬 爱 月 爱情 恋 恋爱 情 心爱 春 春心 喜爱 宠 好 诶 比 西 迪 伊 艾弗 吉 艾尺 艾 杰 开 艾勒 艾马 艾娜 哦 屁 吉吾 艾儿 艾丝 提 伊吾 维 豆贝尔维 艾克斯 吾艾 贼德 零 / 〇 一 二 三 四 五 六 七 八 九 十'))
punctuations=''.join(set('‘ ’ “ ” ‷ ‴ ʾ ʿ ﹕ ﹔ ＊ ％ ！ ＃ ︰ ˜ ˔ ˕ 〃 …'))
kanji=''.join(set('日 一 大 年 会 中 月 本 人 上 子 生 今 高 時 手 米 円 二 社 間 学 後 方 女 心 九 実 万 開 問 動 和 道 意'))
currency=''.join(set('¢ $ € £ ¥ ₰ ₱ ₲ ₳ ₴ ₵ ￥ ﷼ ¤ ƒ ₮ ৲ ৳ ௹ ฿ ៛ ₠ ₡ ₢ ₣ ₤ ₥ ₦ ₧ ₨ ₩ ₪ ₫ ₭ ₯'))
fractions=''.join(set('⅟ ½ ⅓ ⅕ ⅙ ⅛ ⅔ ⅖ ⅚ ⅜ ¾ ⅗ ⅝ ⅞ ⅘ ¼ ⅐ ⅑ ⅒ ↉ % ℅ ‰ ‱'))
korean=''.join(set('ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄸ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅃ ㅄ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅥ ㅦ ㅧ ㅨ ㅻ ㅼ ㅽ ㅾ ㅿ ㆀ ㆁ ㆂ ㆃ ㆄ ㆅ ㅩ ㅪ ㅫ ㅬ ㅭ ㅮ ㅯ ㅰ ㅱ ㅲ ㅳ ㅴ ㅵ ㅶ ㅷ ㅸ ㅹ ㅺ ㅎ ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ'))
latin=''.join(set('ą č Ĥ ħ ĩ Ň Ř Ť Ŵ Ž ⒜ ⒝ ⒞ ⒟ ⒠ ⒡ ⒢ ⒣ ⒤ ⒥ ⒦ ⒧ ⒨ ⒩ ⒪ ⒫ ⒬ ⒭ ⒮ ⒯ ⒰ ⒱ ⒲ ⒳ ⒴ ⒵ Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ Ａ Ｂ Ｃ Ｄ Ｅ Ｆ Ｇ Ｈ Ｉ Ｊ Ｋ Ｌ Ｍ Ｎ Ｏ Ｐ Ｑ Ｒ Ｓ Ｔ Ｕ Ｖ Ｗ Ｘ Ｙ Ｚ ａ ｂ ｃ ｄ ｅ ｆ ｇ ｈ ｉ ｊ ｋ ｌ ｍ ｎ ｏ ｐ ｑ ｒ ｓ ｔ ｕ ｖ ｗ ｘ ｙ ｚ á â æ à å ã ä ç é ê è ð ë í î ì ï ñ ó ô ò ø õ ö ß þ ú û ù ü ý ÿ ᴀ ʙ ᴄ ᴅ ᴇ ғ ɢ ʜ ɪ ᴊ ᴋ ʟ ᴍ ɴ ᴏ ᴏ ᴘ ǫ ʀ s ᴛ ᴜ ᴠ ᴡ x ʏ ᴢ 𝓐 𝓑 𝓒 𝓓 𝓔 ᴭ ᴮ ᴯ ᴰ ᴱ ᴲ ᴳ ᴴ ᴵ ᴶ ᴷ ᴸ ᴹ ᴺ ᴻ ᴼ ᴽ ᴾ ᴿ ᵀ ᵁ ᵂ ᵃ ᵄ ᵆ ᵇ ᵈ ᵉ ᵊ ᵋ ᵌ ᵍ ʱ ʰ ᵢ ᵎ ʲ ᵏ ᵐ ᵑ ᵒ ᵓ ᵔ ᵕ ᵖ ʳ ʴ ᵗ ʵ ᵘ ᵙ ᵛ ᵚ ᵜ ᵝ ᵞ ᵟ ᵠ ᵡ ᶛ ᶜ ᶝ ᶞ ᶟ ᶠ ᶡ ᶢ ᶣ ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᗩ ℊ ℎ ℓ ℘ ℮ ℄ ℇ ℈ ℏ ℔ ℞ ℟ ℣ ℥ Ω ℧ ℩ K Å Ⅎ ℵ ℶ ℷ ℸ ♃ ♄ ☡ ♇ ❡'))
english='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

ultimate=greek+physics+japanese+chinese+punctuations+kanji+currency+fractions+korean+latin+english

length=int(input('Enter Password Length:'))
ultimate=ultimate*length
print(ultimate)
passwordlist=itertools.permutations(ultimate,length)
