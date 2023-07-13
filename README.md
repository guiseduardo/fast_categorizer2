# Fast categorizer 2

A reimplementation of the original Fast categorizer in Qt.

The Fast categorizer is meant to be a tool to quickly sort large unstructured datasets manually into categories. With this tool, something between 2000 to 4000 images can be categorized in an hour.

## New features

* Select multiple classes for the same image;
* Keyboard shortcuts for categories;
* Using Qt as a backend, providing better behavior and customization.

## Usage

Just run `fast_categorizer2` or the `__main__.py` file from the terminal.

1. Use the `config.json` file to point the location of your dataset, where categorized images will be saved and to which categories images will be assigned, along with a **alphabetic** keyboard shortcut (Leave empty with a `""` if you do not wish to use it).

2. Select the category of the displayed image with the buttons on the right or the assigned keyboard shortcut. Multiple categories can be selected. The empty button will unassign any selected categories.

    ![image01](https://github.com/guiseduardo/fast_categorizer2/blob/master/res/01.jpg?raw=true)

3. Once categories are selected, click **Next** or press the right arrow in your keyboard to go to the next image. Likewise, the **Prev** button and the left arrow can be used to go back a frame.

   ![image02](https://github.com/guiseduardo/fast_categorizer2/blob/master/res/02.jpg?raw=true)

4. Once you reach the last image, a message will be printed in the terminal.

   ![image03](https://github.com/guiseduardo/fast_categorizer2/blob/master/res/03.jpg?raw=true)

5. The debug button will print information of currently selected categories for your dataset.

   ![image04](https://github.com/guiseduardo/fast_categorizer2/blob/master/res/04.jpg?raw=true)

6. At any point in your dataset you can quit the program and the categorized images will be sorted to their respective directories. To quit press the **Escape** button or just close the window.

   ![image05a](https://github.com/guiseduardo/fast_categorizer2/blob/master/res/05a.jpg?raw=true)

   ![image05b](https://github.com/guiseduardo/fast_categorizer2/blob/master/res/05b.jpg?raw=true)
