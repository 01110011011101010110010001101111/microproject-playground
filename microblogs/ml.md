# Machine Learning Microblogs!

## Ridge Regression

Sometimes, when finding the optimal fit via $\Theta = (X X^T)^{-1} X Y^T$ (where X and Y are in the machine learning syntax), $X X^T$ could not be invertible. To counter this, we can add a $n\lambda I$ to the array which will make it invertible. You can also add a square penalty of $\lambda \Theta^2$. This will cause $\Theta$ to be smaller and possibly make the fit to the train worse, but it should help with generalization. Note that we generally don't want to have it penalize $\Theta_0$ because it's the intercept and making that smaller is generally not as useful.  
