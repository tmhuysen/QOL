import matplotlib.pyplot as plt

from qollib.DataSet import ConstrainedData


class Grapher:
    def __init__(self, data_set, access_methods, recombinations, recombinations_style = None):
        self.data_set = self.__data_init__(data_set)
        self.access_methods = access_methods
        self.recombinations_style = recombinations_style
        self.recombinations = recombinations

        self.x = 0
        self.y = 1

    def __data_init__(self, data_set):

        if isinstance(data_set, list):
            return data_set
        else:
            return list([data_set])

    def generate_graphs(self):
        figs = list()
        axes = list()

        for i in self.recombinations:
            fig, ax = plt.subplots()
            access_x = self.access_methods[i[self.x]]
            access_y = self.access_methods[i[self.y]]

            for i in self.data_set:
                ax.set(xlabel = access_x(i, name = True), ylabel = access_y(i, name = True))
                label = "lol"
                if self.recombinations_style is not None:
                    ax.plot(access_x(i), access_y(i), *self.recombinations_style, label = label)
                else:
                    ax.plot(access_x(i), access_y(i), linestyle = "", marker = "o", markersize = 0.60)

                ax.grid()

                figs.append(fig)
                axes.append(ax)
        for fig in figs:
            fig.legend()

        return figs


class ConstrainedGrapher(Grapher):
    def __init__(self, constrained_data, recombinations = None):
        if recombinations is None:
            super().__init__(constrained_data,
                             [ConstrainedData.get_energy, ConstrainedData.get_lambda, ConstrainedData.get_population,
                              ConstrainedData.get_entropy], [(1, 0), (1, 2), (2, 0), (2, 3)])
        else:
            super().__init__(constrained_data,
                             [ConstrainedData.get_energy, ConstrainedData.get_lambda, ConstrainedData.get_population,
                              ConstrainedData.get_entropy], recombinations)
