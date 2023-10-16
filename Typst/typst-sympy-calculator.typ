#let hidden(content) = {}

// matrix
#let cmat(..args) = {
  let mat = if (type(args.pos().at(0)) != "array") { (args.pos(),) } else { args.pos() }
  let mat_t = ()
  for j in range(mat.at(0).len()) {
    mat_t.push(())
    for i in range(mat.len()) {
      mat_t.at(j).push(mat.at(i).at(j))
    }
  }
  math.mat(..mat_t)
}

#let eye(n) = {
    let n = if (type(n) == "content") { int(n.text) } else { int(n) }
    let matrix = ()
    for i in range(n) {
        matrix.push(())
        for j in range(n) {
            if (i == j) {
                matrix.at(i).push(1)
            } else {
                matrix.at(i).push(0)
            }
        }
    }
    math.mat(..matrix)
}

#let diag(..args) = {
    let args = args.pos()
    let n = args.len()
    let matrix = ()
    for i in range(n) {
        matrix.push(())
        for j in range(n) {
            if (i == j) {
                matrix.at(i).push(args.at(j))
            } else {
                matrix.at(i).push(0)
            }
        }
    }    
    math.mat(..matrix)
}

// functions
#let derivative(expr, var) = $(dif)/(dif var) expr$
#let sign = math.op("sign")
#let evalat(body) = math.lr(body + "|")

// accents
#let hdot(a) = math.accent(a, math.dot)

#hidden[
```typst-calculator
@func_mat()
def convert_cmat(matrix):
    return sympy.Matrix(matrix).T

@func()
def convert_derivative(expr, var):
    return sympy.Derivative(expr, var)

@func()
def convert_eye(n):
    return sympy.eye(n)

@func()
def convert_diag(*args):
    return sympy.diag(*args)

@func()
def convert_sign(a):
    return sympy.sign(a)
```
]



// --------------------------------------------------

// argmax/min
#let argmax = math.limits($arg max$)
#let argmin = math.limits($arg min$)

// cases
#let when = $"," & quad$;

// vectors and matrices
#let xvec = math.bold("x")
#let yvec = math.bold("y")
#let zvec = math.bold("z")
#let thetavec = math.bold(math.theta)
