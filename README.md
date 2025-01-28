# MICRESS-EarlyStageGrowth

`MICRESS-EarlyStageGrowth` is a Workflow Active Node (WaNo) designed for the [SimStack](https://www.simstack.de) workflow management system. It provides an efficient and user-friendly way to simulate the early-stage growth of materials from a liquid state using [MICRESS](https://www.micress.de), a powerful microstructure simulation software.

This WaNo streamlines the simulation process by allowing users to define all necessary inputs through a graphical user interface (GUI) within SimStack, eliminating the need for manual creation of MICRESS Driving Files. Instead, the required Driving File is automatically generated from a template based on the user inputs, making the process fully transparent and intuitive.

All relevant inputs and outputs, including phase fraction evolution over time, are exported in the SimStack intermediate YAML format via [MicPy](https://docs.micress.de/micpy), ensuring interoperability with other WaNos and facilitating multi-step workflows. By integrating seamlessly with SimStack, `MICRESS-EarlyStageGrowth` simplifies the execution of MICRESS simulations and enables users to build more complex workflows by connecting this WaNo to others, such as for visualization or post-processing.

For a practical demonstration of how this WaNo can be used as part of a complete workflow, including integration with other WaNos, please refer to our [MICRESS SimStack Workflow](https://github.com/lukas-koschmieder/micress-simstack-workflow) example.

## Installation

To set up `MICRESS-EarlyStageGrowth` in your SimStack environment:

1. Clone the repository into your SimStack WaNo directory.
2. Restart the SimStack application to load the new WaNo.

Once installed, `MICRESS-EarlyStageGrowth` will be available for use within the SimStack GUI.
