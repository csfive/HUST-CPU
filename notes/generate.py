def generate(transitions, num_bits, in_prefix="S", out_prefix="N"):
    # 辅助函数：将数字格式化为指定位数的二进制字符串
    def to_bin(n):
        return format(n, f"0{num_bits}b")

    # 动态生成输入变量名列表，例如 4 位时生成 ['S3', 'S2', 'S1', 'S0']
    inputs = [f"{in_prefix}{num_bits - 1 - i}" for i in range(num_bits)]

    # 遍历每一个输出位 (从最高位到最低位)
    for bit_index in range(num_bits):
        out_name = f"{out_prefix}{num_bits - 1 - bit_index}"
        minterms = []

        # 遍历用户定义的每一次状态转换
        for curr_state, next_state in transitions.items():
            curr_bin = to_bin(curr_state)
            next_bin = to_bin(next_state)

            # 如果对应的输出位是 1，则生成一个乘积项 (与逻辑)
            if next_bin[bit_index] == "1":
                term_parts = []
                for j in range(num_bits):
                    if curr_bin[j] == "1":
                        term_parts.append(inputs[j])  # 1 则用原变量
                    else:
                        term_parts.append(f"~{inputs[j]}")  # 0 则加非号

                # 将这一行的输入条件用 '&' 连接
                minterms.append("&".join(term_parts))

        # 将所有乘积项用 '+' 连接。如果全为 0，则输出 0
        if not minterms:
            formula = "0"
        else:
            formula = " + ".join(minterms)

        print(f"{out_name} = {formula}")


if __name__ == "__main__":
    bcd = {i: (i + 1) % 10 for i in range(10)}
    generate(bcd, 4)
