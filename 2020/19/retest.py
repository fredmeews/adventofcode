import re

id42 = "((b(a(bb|ab)|b((a|b)(a|b)))|a(b(bb)|a(bb|a(a|b))))b|(((aa|ab)a|(bb)b)b|(((a|b)a|bb)a)a)a)"
id31 = "(b(b(a(ba)|b(aa))|a(b(ab|(a|b)a)|a(ba|ab)))|a(b((ab|(a|b)a)b|((a|b)a|bb)a)|a((ba)b|(ba|bb)a)))"

m42 = re.compile(id42)
m31 = re.compile(id31)

s = "bbabbbbaabaabba"
m42.match(s)
m42.match(s[5:])

