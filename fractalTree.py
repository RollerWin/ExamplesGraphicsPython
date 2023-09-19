import turtle

branchSize = 5
minBranchSize = 1
mediumBranchSize = 2

treeColor = "brown"
branchColor = "green"

angleBetweenBranches = 30
extendedAngleBetweenBranches = 60

brush = turtle.Turtle()
brush.left(90)
brush.speed(200)
brush.pensize(branchSize)
brush.color(treeColor)
brush.shape("turtle")

def tree(i, branchSize):
    if i < 10:
        return
    else:
        branchSize = branchSize - 1 if branchSize > minBranchSize else minBranchSize
        brush.pensize(branchSize)
        
        if branchSize == minBranchSize:
            brush.color(branchColor)
        else:
            brush.color(treeColor)

        brush.forward(i)

        if branchColor in brush.color():
            brush.dot(10)

        brush.right(angleBetweenBranches)
        tree(3 * i / 4, branchSize)
        
        if branchSize > mediumBranchSize:
            brush.left(angleBetweenBranches)
            tree(3 * i / 4, branchSize)
            brush.left(angleBetweenBranches)
        else:
            brush.left(extendedAngleBetweenBranches)

        tree(3 * i / 4, branchSize)
        brush.right(angleBetweenBranches)
        brush.backward(i)


tree(100, branchSize)
turtle.done()