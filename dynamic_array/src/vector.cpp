

#include <vector>

static double average(std::vector<double> vect)
{
    double total = 0;
    for(const auto& elem : vect)
    {
        total += elem;
    }
    return total / vect.size();
}