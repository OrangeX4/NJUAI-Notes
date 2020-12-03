$$
\frac{3+n}{n^2+n+2} < \varepsilon
$$

---

$$
\frac{2}{n} < \varepsilon
$$

---

$$
n > 关于\varepsilon的表达式
$$

---

$$
N = [ \ 关于\varepsilon的表达式 \ ]
$$

---

$$
\begin{aligned}
& \ \quad \left|\frac{4n+1}{3n+1} -\frac{4}{3} \right| \\
&<\left|\frac{4n+1}{3n} -\frac{4}{3} \right| \\
&=\left|\frac{4}{3}+ \frac{1}{3n} -\frac{4}{3} \right| \\
&=\left|\frac{1}{3n} \right| \\
&=\frac{1}{3n} \\
&< \varepsilon \\
\\
&则 n > \frac{1}{3\varepsilon} \\
&即 n > N = \left|\frac{1}{3\varepsilon} \right| 
\end{aligned}
$$

---

            3   13
        1   -3  1
    --------------
    3   4   -5  6
    3   -9  3
    --------------
        13  -8  6
        13  -39 13
        ----------
            31  -7

---

                    1   1
        1   2       1   2
    ----------------------
    1   3   1   1   3   1
    1   2       1   2
    ----------------------
        1   1       1   1
        1   2       1   2
        ------------------
            -1          -1


---

$$
\begin{aligned}
\lim_{x\to 0^+}[\frac{(1+x)^{\frac{1}{x}}}{e}]^{\frac{1}{x}}
&=\lim_{x\to 0^+}\exp[\frac{1}{x}(\frac{1}{x}\ln(1+x)-1)] \\
&=\lim_{x\to 0^+}\exp(\frac{1}{x^2}\ln(1+x)-\frac{1}{x}) \\
&=\lim_{x\to 0^+}\exp(\frac{\ln(1+x)-x}{x^2}) \\
&=\lim_{x\to 0^+}\exp(\frac{(x-\frac{x^2}{2})-x}{x^2}) \\
&=e^{-\frac{1}{2}} \\
\end{aligned}
$$

$$
\begin{aligned}
\lim_{x\to 0^+}[\frac{(1+x)^{\frac{1}{x}}}{e}]^{\frac{1}{x}}=\lim_{x\to 0^+}\frac{(1+x)^{\frac{1}{2x}}}{e^{\frac{1}{x}}}
\end{aligned}
$$


---

