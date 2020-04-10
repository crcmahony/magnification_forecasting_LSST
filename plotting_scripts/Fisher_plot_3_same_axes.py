from __future__ import print_function, division
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.lines as ml
from matplotlib.patches import Ellipse
import matplotlib.gridspec as gridspec
import scipy.stats
norm = scipy.stats.norm

pdf_baseline = lambda l, s: np.linspace( norm.ppf(0.01, loc=l, scale=s), norm.ppf(0.99, loc=l, scale=s), 100 )
minmax = lambda x: (x.min(), x.max())

def tick_ranger(data_range, nticks=5, short=0, **kwargs):
        # this bit is rubbish ###
        def short_range(mid=0, step=0.05, **kwargs):
                mid_up = np.arange(mid, data_range.max()+step, step=step)
                mid_down = np.arange(data_range.min()-step, mid+step, step=step)
                return np.concatenate((mid_up, mid_down))
        if short:
                ticks = short_range(**kwargs)
                #ticks = [myround(t) for t in ticks]
                tlabs = ["%.2f"%t for t in ticks]
        #########################
        else:
                # makes tick labels to 3dp and removes the first and last
                # so for 3 labels, feed nticks=5
                ticks = np.linspace(data_range.min(), data_range.max(), nticks)
                tlabs = ["%.3f"%t for t in ticks]
        tlabs = [tl.rstrip('0') for tl in tlabs]
        tlabs[0] = tlabs[-1] = ''
        return ticks, tlabs

def make_plot_grid(params, labsz):
    # tick and axis label-sizes
    mpl.rcParams['xtick.labelsize'] = 14
    mpl.rcParams['ytick.labelsize'] = 14
    mpl.rcParams['axes.labelsize'] = labsz

    # feed a list of parameter axis labels
    # length of which sets size of plot array
    nparam = len(params)
    print('nparam = %s'%nparam)

    f = plt.figure(figsize=(18,18))
    gs = gridspec.GridSpec(nparam, nparam)
    axes = []
    axids = []
    for x in range(nparam):
        for y in range(nparam):
                        # axis keys of form eg. ax0112 for x=1, y=12
                        axid = 'ax%s%s' % (str(x).zfill(2), str(y).zfill(2))
                        # skip if inverse...
                        if 'ax%s%s'%(str(y).zfill(2), str(x).zfill(2)) in axids:
                                continue
                        # ...create axis if not
                        ax = plt.subplot(gs[y, x])
                        if (y!=(nparam-1)): # | ((y==(nparam-1))&(x==(nparam-1))):
                                # take x-tick labels off for all but bottom row
                                plt.setp(ax.get_xticklabels(), visible=False)
                        else:
                                # and label last row of x-axes
                                ax.set_xlabel("%s"%(params[:nparam][x]))
                        if x!=0 | ((x==0)&(y==0)):
                                # take y-tick labels off for all but first column
                                plt.setp(ax.get_yticklabels(), visible=False)
                        else:
                                # and label first column
                                ax.set_ylabel("%s"%(params[:nparam][y]))
                        if x==y:
                                # take y-ticks off for 1-d marginals
                                ax.tick_params(left=0, right=0)
                        # append to axis list and key list so that inverse is skipped
                        axes.append(ax)
                        axids.append(axid)
    plt.tight_layout()
    plt.subplots_adjust(wspace=0, hspace=0)
    # return dictionary where axis keys point to the axis instance
    return dict(zip(axids, axes))

def fisher_grid(cov_array, cov_array2, cov_array3, maxlikes, axes=None, params=None, labelsize=26, cov_color='r', cov2_color='b', cov3_color='g', **kwargs):

        # check cov inputs
        if type(cov_array) == np.ndarray:
                cov = cov_array
                cov2 = cov_array2
                cov3 = cov_array3
                nparams = len(cov)
                param_ids = range(nparams)
        else:
                print("unrecognised fisher type, must be numpy ndarray")
                sys.exit()

        # create axes
        axes = make_plot_grid(params, labsz=labelsize)
 
        keys = []
        ells = {}
        ells2 = {}
        ells3 = {}

        for i in param_ids:
                stri = str(i).zfill(2)
                for j in param_ids:
                        strj = str(j).zfill(2)

                        # make axis keys as above
                        key = '%s%s' % (stri, strj)
                        if '%s%s' % (strj, stri) in keys:
                                continue

                        # axk = axes_dict[axis_key]
                        axk = axes['ax'+key]
                        # here I feed the parameter mean from MCMC - usually construct a .pickle dict with keys:values e.g. '0000':0.286 for Omega_m etc.
                        x_mean = maxlikes["%s%s" % (stri, stri)]
                        y_mean = maxlikes["%s%s" % (strj, strj)]
                        # variance from fisher matrix^-1
                        x_var = cov[i, i]
                        y_var = cov[j, j]
                        x_var2 = cov2[i, i]
                        y_var2 = cov2[j, j]
                        x_var3 = cov3[i, i]
                        y_var3 = cov3[j, j]

                        # define 0.01 - 0.99 baseline for pdf
                        x_baseline = pdf_baseline(x_mean, x_var**0.5)
                        y_baseline = pdf_baseline(y_mean, y_var**0.5)

                        x_baseline2 = pdf_baseline(x_mean, x_var2**0.5)
                        y_baseline2 = pdf_baseline(y_mean, y_var2**0.5)

                        x_baseline3 = pdf_baseline(x_mean, x_var3**0.5)
                        y_baseline3 = pdf_baseline(y_mean, y_var3**0.5)

                        # define Gaussian pdf
                        pdf = norm.pdf(x_baseline, loc=x_mean, scale=x_var**0.5)
                        pdf2 = norm.pdf(x_baseline2, loc=x_mean, scale=x_var2**0.5)
                        pdf3 = norm.pdf(x_baseline3, loc=x_mean, scale=x_var3**0.5)

                        # normalise pdf
                        pdf /= np.trapz(pdf, x_baseline)
                        pdf2 /= np.trapz(pdf2, x_baseline2)
                        pdf3 /= np.trapz(pdf3, x_baseline3)

                        # same function I previously sent
                        ells[key] = ellipses_2sigma(cov, (i,j), xy=(x_mean, y_mean), **kwargs)
                        ells2[key] = ellipses_2sigma(cov2, (i,j), xy=(x_mean, y_mean), **kwargs)
                        ells3[key] = ellipses_2sigma(cov3, (i,j), xy=(x_mean, y_mean), **kwargs)

                        if i!=j:
                                # for off-diagonals, plot ellipses:
                                grid_ells(ells[key], axk, c=cov_color, lw=2.0, a=1.0)
                                grid_ells(ells2[key], axk, c=cov2_color, lw=2.0, a=1.0)
                                grid_ells(ells3[key], axk, c=cov3_color, lw=2.0, a=1.0)

                                # axis limits according to pdf baseline
                                axk.set_ylim(minmax(y_baseline))
                                y_ticks, y_tlabs = tick_ranger(y_baseline)
                                axk.set_yticks( y_ticks )
                                axk.set_yticklabels( y_tlabs )
                        else:
                                # on-diagonals, plot gauss pdfs
                                axk.plot(x_baseline, pdf, c=cov_color, lw=2.0)
                                axk.plot(x_baseline2, pdf2, c=cov2_color, lw=2.0)
                                axk.plot(x_baseline3, pdf3, c=cov3_color, lw=2.0)

                        axk.set_xlim(minmax(x_baseline))
                        x_ticks, x_tlabs = tick_ranger(x_baseline)
                        axk.set_xticks( x_ticks )
                        axk.set_xticklabels( x_tlabs )
                        # append keys as before, for skipping inverses
                        keys.append(key)

        return plt.gcf(), axes

def grid_ells(ells, ax, c='c', a=0.3, lw=1.5, ls='-'):
        # feed this function with lists/tuples of ellipse artists from
        # ellipses_2sigma(), and an Axes instance on which to plot
        for ell in ells:
                ax.add_artist(ell)
                ell.set_clip_box(ax.bbox)
                ell.set_alpha(a)
                ell.set_facecolor('none')
                ell.set_edgecolor(c)
                ell.set_linewidth(lw)
                ell.set_linestyle(ls)
                #ell.set_facecolor(fc)

def ellipses_2sigma(cov, ids, xy=(-1.019, 0.0)):
        ells = {} 
        for i in np.arange(2)+1:
                print(i)
                i = int(i)
                a, b, t, a_width = ellipse_params(cov, ids, CLsigma=i)
                print(a_width)
                if a_width:
                        ells['ell'+str(i)] = Ellipse(xy=xy, width=a, height=b, angle=t)
                else:
                        ells['ell'+str(i)] = Ellipse(xy=xy, width=b, height=a, angle=t)
        return ells['ell1'], ells['ell2']

def ellipse_params(cov, ids, CLsigma=1):
        id1, id2 = ids
        alpha = {1:1.52, 2:2.48, 3:3.44} # ellipse axis scalings corresponding to sigma-confidence levels
        alpha = alpha[CLsigma]
        var1, var2, var12 = cov[id1, id1], cov[id2, id2], cov[id1, id2]
        a = np.sqrt( (var1 + var2)/2. + np.sqrt( 0.25*(var1 - var2)**2 + var12**2 ) )
        b = np.sqrt( (var1 + var2)/2. - np.sqrt( 0.25*(var1 - var2)**2 + var12**2 ) )
        a *= 2.*alpha
        b *= 2.*alpha
        tan2th = (2.*var12)/(var1 - var2)
        theta = np.arctan(tan2th)/2.
        theta *= (180./np.pi)

        # python class 'Ellipse' rotates through theta[deg], anti-clockwise,
        # therefore a +ve correlation & +ve calculated theta
        # means that a(semi-major) is along the x-axis, and so on;
        R = pearson_r(cov.copy())
        if (R[id1, id2] > 0) == (theta > 0):
                a_width = 1
        else:
                a_width = 0

        return a, b, theta, a_width

def pearson_r(covar_matrix):
        # just a function to return the correlation matrix
        # be sure to call on COPIES of covar, else original
        # will be changed!
        c = covar_matrix
        d = np.diag(c)
        stddev = np.sqrt(d.real)
        c /= stddev[:, None]
        c /= stddev[None, :]
        # Clip real and imaginary parts to [-1, 1]
        np.clip(c.real, -1, 1, out=c.real)
        if np.iscomplexobj(c):
            np.clip(c.imag, -1, 1, out=c.imag)
        return c
