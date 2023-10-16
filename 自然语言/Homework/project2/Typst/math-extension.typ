// Math display
#let display(body) = {
    if (repr(body.func()) == "equation") {
        if (body.block) {
            $#box(body)$
        } else {
            panic("The equation must be a block")
        }
    } else {
        panic("The content is not a equation")
    }
}

// eval at
#let evalat(body) = math.lr(body + "|")

// displaystyle
#let dsum = math.limits(math.sum)
#let dproduct = math.limits(math.product)

// argmax/min
#let argmax = math.limits($arg max$)
#let argmin = math.limits($arg min$)

// other functions
#let sign = math.op("sign")

// short name
#let to = math.arrow.r
#let ot = math.arrow.l
#let implies = math.arrow.r.double

#let when = $"," & quad$

// vectors and matrices
#let xvec = math.bold("x")
#let yvec = math.bold("y")
#let zvec = math.bold("z")
#let thetavec = math.bold(math.theta)