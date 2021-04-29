#ifndef FLVMI_H
#define FLVMI_H
#include"../optimizers/NaiveGreedyOptimizer.h"
#include"../optimizers/LazyGreedyOptimizer.h"
#include"../optimizers/StochasticGreedyOptimizer.h"
#include"../optimizers/LazierThanLazyGreedyOptimizer.h"
#include"../SetFunction.h"
#include <unordered_set>

class FacilityLocationVariantMutualInformation : public SetFunction {
    protected:
    ll n;  
    int numQueries;
    float magnificationLambda;
    std::vector<std::vector <float> > kernelQuery;   //n X numQueries

    std::vector<float> similarityWithNearestInX;
    std::vector<float> qMaxMod;

   public:
    FacilityLocationVariantMutualInformation(ll n_, int numQueries_, std::vector<std::vector<float>> const &kernelQuery_, float magnificationLambda_);

    double evaluate(std::unordered_set<ll> const &X);
	double evaluateWithMemoization(std::unordered_set<ll> const &X);
	double marginalGain(std::unordered_set<ll> const &X, ll item);
	double marginalGainWithMemoization(std::unordered_set<ll> const &X, ll item);
	void updateMemoization(std::unordered_set<ll> const &X, ll item);
    std::unordered_set<ll> getEffectiveGroundSet();
	std::vector<std::pair<ll, double>> maximize(std::string, ll budget, bool stopIfZeroGain, bool stopIfNegativeGain, float epsilon, bool verbose);
    void clearMemoization();
	void setMemoization(std::unordered_set<ll> const &X);
    // FacilityLocationVariantMutualInformation* clone();
};
#endif