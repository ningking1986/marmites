from mbase import package

class mfoc(package):
    'Output control package'
    def __init__(self, model, ihedfm=0, iddnfm=0, item2=[[0,1,0,1]], item3=[[0,0,1,0]], \
                 extension=['oc','cbc','hds','ddn'], unitnumber=[14, 50, 51, 52]):
        package.__init__(self, model, extension, ['OC', 'DATA(BINARY)', 'DATA(BINARY)', 'DATA(BINARY)'], unitnumber) # Call ancestor's init to set self.parent, extension, name and unit number
        self.heading = '# Output control package file for MODFLOW-2000, generated by Flopy.'
        self.url = 'oc.htm'
        self.ihedfm = ihedfm
        self.iddnfm = iddnfm
        dummy, self.item2 = self.assign_layer_row_column_data(item2, 4)
        #dummy, self.item3 = self.assign_layer_row_column_data(item3, 4)
        if (item2 != None):
            error_message = 'item2 must have 4 columns'
            if (not isinstance(item2, list)):
                item2 = [item2]
            for a in item2:
                assert len(a) == 4, error_message
            self.item2 = item2
        if (item3 != None):
            error_message = 'item3 must have 4 columns'
            if (not isinstance(item3, list)):
                item3 = [item3]
            for a in item3:
                assert len(a) == 4, error_message
            self.item3 = item3
        #assert (self.item2[0] > 0).any(), 'This option is not supported yet.'
        self.parent.add_package(self)
    def __repr__( self ):
        return 'Output control package class'
    def write_file(self):
        # Open file for writing
        f_oc = open(self.fn_path, 'w')
        f_oc.write('%s\n' % self.heading)
        f_oc.write('%3i%3i%5i%5i\n' % (self.ihedfm, self.iddnfm, self.unit_number[2], self.unit_number[3]))
        nstp = self.parent.get_package('DIS').nstp
        ss = 0
        for p in range(len(nstp)): #len(nstp) is the number of stress periods
            for s in range(nstp[p]):
                if (ss < len(self.item2)):
                    a = self.item2[ss]
                else:
                    a = self.item2[-1]
                if (ss < len(self.item3)):
                    b = self.item3[ss]
                else:
                    b = self.item3[-1]
                f_oc.write('%3i%3i%3i%3i  Period %3i, step %3i\n' % (a[0], a[1], a[2], a[3], p + 1, s + 1) )
                f_oc.write('%3i%3i%3i%3i\n' % (b[0], b[1], b[2], b[3]) )
                ss = ss + 1
        f_oc.close()