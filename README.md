# Catastrophic-risk-aware reinforcement learning with extreme-value-theory-based policy gradients

## Abstract

This paper tackles the problem of mitigating catastrophic risk (which is risk with very
low frequency but very high severity) in the context of a sequential decision making process.
This problem is particularly challenging due to the scarcity of observations in the far tail
of the distribution of cumulative costs (negative rewards). A policy gradient algorithm is
developed, that we call POTPG. It is based on approximations of the tail risk derived from
extreme value theory. Numerical experiments highlight the out-performance of our method
over common benchmarks, relying on the empirical distribution. An application to financial
risk management, more precisely to the dynamic hedging of a financial option, is presented

The 'GPD_convergence' generate the simulation experiments conducted in a controlled environment, and the 'NIG_Gammahedging' provide the application of our method in financial hedging.

'cvar_plot' will plot our objective function (CVaR$_{0.999}$ of the hedging shortfall) versus the hedge ratio $\theta$, representing the percentage of the target option Gamma being neutralized. Estimates are obtained with brute force calculations, i.e.~through sample averaing over $1,\!000,\!000$ simulated paths.
