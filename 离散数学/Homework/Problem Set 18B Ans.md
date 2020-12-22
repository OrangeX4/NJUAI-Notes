# Problem 1

(1) $K_n对于任意n值均是正则图$

(2) $W_n对于n=3时是正则图$

(3) $Q_n对于任意n值均是正则图$


# Problem 2

$下右图(1)的补图如图(2), 经过变形后得图(3), 可以与图(4)一一对应$

![](2020-12-22-00-11-12.png)

$$
\begin{aligned}
即构造f=\{& \\
&\quad(a, B), (b, E), (c, C), (d, H), (e, D), (f, G), (g, A), (h, F), \\
&\quad(ab, BE), (bc, EC), (cd, CH), (da, HB), \\
&\quad(ae, BD), (bf, EG), (cg, CA), (dh, HF), \\
&\quad(ef, DG), (fg, GA), (gh, AF), (he, FD), \\
&\} \\
\end{aligned}
$$

$即可知f满足使得两图同构的条件$


# Problem 3

$G\simeq H\Rightarrow \overline{G}\simeq \overline{H}:$

$\because G\cup \overline{G}=H\cup\overline{H}=K_n, G\simeq H$

$\therefore G, H, \overline{G}, \overline{H}的阶数都是相同的$

$对于任意一条边e\in K_n,$

$若e\not\in E_{\overline{G}}, 即\gamma_{\overline{G}}(e)=\{v_i, v_j\}不存在$

$我们假设此时\gamma_{\overline{H}}(e)=\{f(v_i), f(v_j)\}存在,$
$则由补图定义我们有\gamma_{G}(e)=\{v_i, v_j\}存在而\gamma_{H}(e)=\{f(v_i), f(v_j)\}不存在, 与G\simeq H矛盾$

$因此我们有\gamma_{\overline{G}}(e)=\{v_i, v_j\}和\gamma_{\overline{H}}(e)=\{f(v_i), f(v_j)\}不可能同时存在$

$若e\in E_{\overline{G}}, 同理我们可知\gamma_{\overline{G}}(e)=\{v_i, v_j\}和\gamma_{\overline{H}}(e)=\{f(v_i), f(v_j)\}不可能同时不存在$

$即\gamma_{\overline{G}}(e)=\{v_i, v_j\}\Leftrightarrow \gamma_{\overline{H}}(e)=\{f(v_i), f(v_j)\}$

$\therefore 我们有\overline{G}\simeq \overline{H}$

$\overline{G}\simeq \overline{H}\Rightarrow G\simeq H:$

$同上述论证, 同理可知成立$


# Problem 4

