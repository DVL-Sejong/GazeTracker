from database import constant
from objects.object import Size, Geometry, Point
from objects.GazeTuple import GazeTuple


class GazeData:
    def __init__(self, window):
        self.window = window
        self.screen_size = Size(0, 0)
        self.display_geometry = Geometry(Point(0, 0, 0), Size(0, 0))
        self.paint_geometry = Geometry(Point(0, 0, 0), Size(0, 0))
        self.data = []
        self.t_index = []
        self.t_order = []

    def synchronize_geometries(self, window, display, paint):
        self.screen_size.set(window)
        self.display_geometry.set(display)
        self.paint_geometry.set(paint.geometry())

    def add_tuple(self, tuple):
        element = GazeTuple(tuple)
        element.initialize(self.screen_size, self.paint_geometry.point, self.display_geometry)
        self.data.append(element)

    def order_in_time(self):
        time_first = self.data[0].timestamp
        time_index = 0
        time_order = -1

        for i in range(len(self.data)):
            if self.data[i].timestamp - time_first >= 1000000:
                time_first = self.data[i].timestamp
                time_index += 1
                time_order = 0
                t_index = time_index
                t_order = time_order
            else:
                time_order += 1
                t_index = time_index
                t_order = time_order

            self.t_index.append(t_index)
            self.t_order.append(t_order)

    def save(self, dbconn):
        for i in range(len(self.data)):
            tuple = {
                'id': self.data[i].id,
                'width': self.paint_geometry.size.width,
                'height': self.paint_geometry.size.height,
                'left_x': self.data[i].left_point.x,
                'left_y': self.data[i].left_point.y,
                'right_x': self.data[i].right_point.x,
                'right_y': self.data[i].right_point.x,
                't': self.t_index[i],
                't_order': self.t_order[i],
                'left_validity': self.data[i].left_point.validity,
                'right_validity': self.data[i].right_point.validity
            }

            dbconn.insert(table=constant.TABLE, data=tuple)
