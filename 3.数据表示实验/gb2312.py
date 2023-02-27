str = "１２３４５ＡＢＣＤＥＦＧａｂｃｄｅｆｇ轻轻的我走了，正如我轻轻的来；我轻轻的招手，作别西天的云彩。那河畔的金柳，是夕阳中的新娘；波光里的艳影，在我的心头荡漾。"
gb2312_str = str.encode("gb2312")

hex_str = ""
for i in range(len(gb2312_str)):
    if i % 2 == 0:
        hex_str += " "
    hex_str += f"{gb2312_str[i]:02X}"

with open("gb2312.txt", "w") as file:
    file.write(hex_str)
