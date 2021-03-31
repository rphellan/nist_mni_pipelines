#
# @author Renzo Phellan
# @date 18/02/2021
#

import os
import argparse
from ipl.lp.preprocess import *
from ipl.lp.registration import *
from ipl.lp.resample import *
from ipl.lp.segment import *
from ipl.lp.structures import *
from ipl.lp.utils import *
from ipl.minc_tools import mincTools
from string import Template

def save_scene(images_list, minc_dir, file_path):
    """
    Save a scene containing the volumes calculated by the pipeline.
    The volumes are the registered head image, the brain mask, the cortex
    surface, and the skin surface. The scene is stored in fname.

    Arguments: images_list Dictionary containing images
               minc_dir Directory where minc images are saved
               file_path Path of the output scene file
    """

    #Set xml structure

    default_xml = Template(
    """<!DOCTYPE configML>
<configuration>
 <SaveScene>
  <IbisVersion value="3.0.0  Dev"/>
  <IbisRevision value="09fdb78"/>
  <Version value="6.0"/>
  <NextObjectID value="7"/>
  <NumberOfSceneObjects value="9"/>
  <ObjectList>
   <ObjectInScene_0>
    <ObjectClass value="WorldObject"/>
    <FullFileName value="none"/>
    <ObjectID value="-2"/>
    <ParentID value="-1"/>
    <ObjectName value="World"/>
    <AllowChildren value="1"/>
    <AllowChangeParent value="0"/>
    <ObjectManagedBySystem value="1"/>
    <ObjectHidden value="0"/>
    <AllowHiding value="0"/>
    <ObjectDeletable value="0"/>
    <NameChangeable value="0"/>
    <ObjectListable value="1"/>
    <AllowManualTransformEdit value="0"/>
    <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
   </ObjectInScene_0>
   <ObjectInScene_1>
    <ObjectClass value="TripleCutPlaneObject"/>
    <FullFileName value="none"/>
    <ObjectID value="-3"/>
    <ParentID value="-2"/>
    <ViewPlanes value="0 0 0 "/>
    <PlanesPosition value="-3.8772645601035691e+00 -1.2849156404889982e+01 1.8000000000000000e+01 "/>
    <SliceThickness value="1"/>
    <SliceMixMode>
     <NumberOfElements value="3"/>
     <Element_0 value="2"/>
     <Element_1 value="2"/>
     <Element_2 value="2"/>
    </SliceMixMode>
    <BlendingModeIndices>
     <NumberOfElements value="3"/>
     <Element_0 value="2"/>
     <Element_1 value="2"/>
     <Element_2 value="2"/>
    </BlendingModeIndices>
   </ObjectInScene_1>
   <ObjectInScene_2>
    <ObjectClass value="VolumeRenderingObject"/>
    <FullFileName value="none"/>
    <ObjectID value="-5"/>
    <ParentID value="-2"/>
    <ObjectName value="PRISM Volume Render"/>
    <AllowChildren value="0"/>
    <AllowChangeParent value="0"/>
    <ObjectManagedBySystem value="1"/>
    <ObjectHidden value="1"/>
    <AllowHiding value="1"/>
    <ObjectDeletable value="0"/>
    <NameChangeable value="0"/>
    <ObjectListable value="1"/>
    <AllowManualTransformEdit value="0"/>
    <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
    <IsAnimating value="0"/>
    <SamplingDistance value="1.0000000000000000e+00"/>
    <ShowInteractionWidget value="0"/>
    <InteractionWidgetLine value="0"/>
    <InteractionPoint1 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 "/>
    <InteractionPoint2 value="2.0000000000000000e+02 0.0000000000000000e+00 0.0000000000000000e+00 "/>
    <RayInitShaderTypeName value="None"/>
    <StopConditionShaderTypeName value="ERT alpha 99%"/>
    <ImageSlots>
     <NumberOfElements value="1"/>
     <Element_0>
      <VolumeEnabled value="1"/>
      <VolumeIs16Bits value="0"/>
      <LinearSampling value="1"/>
      <ShaderContributionTypeName value="Add"/>
      <LastImageObjectId value="4"/>
      <ColorTransferFunction>
       <NbColorPoints value="2"/>
       <ColorPoint_0 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
       <ColorPoint_1 value="2.5500000000000000e+02 1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
      </ColorTransferFunction>
      <OpacityTransferFunction>
       <NbPoints value="2"/>
       <Point_0 value="0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
       <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
      </OpacityTransferFunction>
     </Element_0>
    </ImageSlots>
   </ObjectInScene_2>
   <ObjectInScene_3>
    <ObjectClass value="SceneObject"/>
    <FullFileName value="none"/>
    <ObjectID value="0"/>
    <ParentID value="-2"/>
    <ObjectName value="ELECTRODES"/>
    <AllowChildren value="1"/>
    <AllowChangeParent value="1"/>
    <ObjectManagedBySystem value="0"/>
    <ObjectHidden value="1"/>
    <AllowHiding value="1"/>
    <ObjectDeletable value="1"/>
    <NameChangeable value="1"/>
    <ObjectListable value="1"/>
    <AllowManualTransformEdit value="1"/>
    <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
   </ObjectInScene_3>
   <ObjectInScene_4>
    <ObjectClass value="SceneObject"/>
    <FullFileName value="none"/>
    <ObjectID value="1"/>
    <ParentID value="0"/>
    <ObjectName value="Electrodes (Ref)"/>
    <AllowChildren value="1"/>
    <AllowChangeParent value="1"/>
    <ObjectManagedBySystem value="0"/>
    <ObjectHidden value="0"/>
    <AllowHiding value="1"/>
    <ObjectDeletable value="1"/>
    <NameChangeable value="1"/>
    <ObjectListable value="1"/>
    <AllowManualTransformEdit value="1"/>
    <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
   </ObjectInScene_4>
   <ObjectInScene_5>
    <ObjectClass value="SceneObject"/>
    <FullFileName value="none"/>
    <ObjectID value="2"/>
    <ParentID value="0"/>
    <ObjectName value="Saved Elect"/>
    <AllowChildren value="1"/>
    <AllowChangeParent value="1"/>
    <ObjectManagedBySystem value="0"/>
    <ObjectHidden value="0"/>
    <AllowHiding value="1"/>
    <ObjectDeletable value="1"/>
    <NameChangeable value="1"/>
    <ObjectListable value="1"/>
    <AllowManualTransformEdit value="1"/>
    <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
   </ObjectInScene_5>
   <ObjectInScene_6>
    <ObjectClass value="ImageObject"/>
    <FullFileName value="./$replace_brain_image_path"/>
    <ObjectID value="4"/>
    <ParentID value="-2"/>
    <ObjectName value="$replace_brain_image_name"/>
    <AllowChildren value="1"/>
    <AllowChangeParent value="1"/>
    <ObjectManagedBySystem value="0"/>
    <ObjectHidden value="0"/>
    <AllowHiding value="1"/>
    <ObjectDeletable value="1"/>
    <NameChangeable value="1"/>
    <ObjectListable value="1"/>
    <AllowManualTransformEdit value="1"/>
    <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
    <LabelImage value="0"/>
    <ViewOutline value="0"/>
    <LutIndex value="0"/>
    <LutRange value="-9.5372891426086426e-01 4.1060385131835938e+02 "/>
    <IntensityFactor value="1.0000000000000000e+00"/>
    <VolumeRenderingEnabled value="0"/>
    <ColorWindow value="1.0000000000000000e+00"/>
    <ColorLevel value="5.0000000000000000e-01"/>
    <EnableShading value="0"/>
    <Ambiant value="1.0000000000000001e-01"/>
    <Diffuse value="6.9999999999999996e-01"/>
    <Specular value="2.0000000000000001e-01"/>
    <SpecularPower value="1.0000000000000000e+01"/>
    <EnableGradientOpacity value="1"/>
    <AutoSampleDistance value="1"/>
    <SampleDistance value="1.0000000000000000e+00"/>
    <ShowVolumeClippingBox value="0"/>
    <VolumeRenderingBounds value="-9.6000000000000000e+01 9.6000000000000000e+01 -1.3200000000000000e+02 9.6000000000000000e+01 -7.8000000000000000e+01 1.1400000000000000e+02 "/>
    <ScalarOpacity>
     <NbPoints value="2"/>
     <Point_0 value="0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </ScalarOpacity>
    <GradientOpacity>
     <NbPoints value="2"/>
     <Point_0 value="0.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </GradientOpacity>
    <ColorTransferFunction>
     <NbColorPoints value="2"/>
     <ColorPoint_0 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <ColorPoint_1 value="2.5500000000000000e+02 1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </ColorTransferFunction>
   </ObjectInScene_6>
   <ObjectInScene_7>
    <ObjectClass value="ImageObject"/>
    <FullFileName value="./$replace_head_image_ct_path"/>
    <ObjectID value="5"/>
    <ParentID value="-2"/>
    <ObjectName value="$replace_head_image_ct_name"/>
    <AllowChildren value="1"/>
    <AllowChangeParent value="1"/>
    <ObjectManagedBySystem value="0"/>
    <ObjectHidden value="0"/>
    <AllowHiding value="1"/>
    <ObjectDeletable value="1"/>
    <NameChangeable value="1"/>
    <ObjectListable value="1"/>
    <AllowManualTransformEdit value="1"/>
    <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
    <LabelImage value="0"/>
    <ViewOutline value="0"/>
    <LutIndex value="0"/>
    <LutRange value="-8.5804863281250000e+03 3.3295343750000000e+04 "/>
    <IntensityFactor value="1.0000000000000000e+00"/>
    <VolumeRenderingEnabled value="0"/>
    <ColorWindow value="1.0000000000000000e+00"/>
    <ColorLevel value="5.0000000000000000e-01"/>
    <EnableShading value="0"/>
    <Ambiant value="1.0000000000000001e-01"/>
    <Diffuse value="6.9999999999999996e-01"/>
    <Specular value="2.0000000000000001e-01"/>
    <SpecularPower value="1.0000000000000000e+01"/>
    <EnableGradientOpacity value="1"/>
    <AutoSampleDistance value="1"/>
    <SampleDistance value="1.0000000000000000e+00"/>
    <ShowVolumeClippingBox value="0"/>
    <VolumeRenderingBounds value="-9.6000000000000000e+01 9.6000000000000000e+01 -1.3200000000000000e+02 9.6000000000000000e+01 -7.8000000000000000e+01 1.1400000000000000e+02 "/>
    <ScalarOpacity>
     <NbPoints value="2"/>
     <Point_0 value="0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </ScalarOpacity>
    <GradientOpacity>
     <NbPoints value="2"/>
     <Point_0 value="0.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </GradientOpacity>
    <ColorTransferFunction>
     <NbColorPoints value="2"/>
     <ColorPoint_0 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <ColorPoint_1 value="2.5500000000000000e+02 1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </ColorTransferFunction>
   </ObjectInScene_7>
   <ObjectInScene_8>
    <ObjectClass value="ImageObject"/>
    <FullFileName value="./$replace_head_image_mr_path"/>
    <ObjectID value="6"/>
    <ParentID value="-2"/>
    <ObjectName value="$replace_head_image_mr_name"/>
    <AllowChildren value="1"/>
    <AllowChangeParent value="1"/>
    <ObjectManagedBySystem value="0"/>
    <ObjectHidden value="0"/>
    <AllowHiding value="1"/>
    <ObjectDeletable value="1"/>
    <NameChangeable value="1"/>
    <ObjectListable value="1"/>
    <AllowManualTransformEdit value="1"/>
    <LocalTransform value="1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
    <LabelImage value="0"/>
    <ViewOutline value="0"/>
    <LutIndex value="0"/>
    <LutRange value="-1.1596175432205200e+00 4.4860403442382813e+02 "/>
    <IntensityFactor value="1.0000000000000000e+00"/>
    <VolumeRenderingEnabled value="0"/>
    <ColorWindow value="1.0000000000000000e+00"/>
    <ColorLevel value="5.0000000000000000e-01"/>
    <EnableShading value="0"/>
    <Ambiant value="1.0000000000000001e-01"/>
    <Diffuse value="6.9999999999999996e-01"/>
    <Specular value="2.0000000000000001e-01"/>
    <SpecularPower value="1.0000000000000000e+01"/>
    <EnableGradientOpacity value="1"/>
    <AutoSampleDistance value="1"/>
    <SampleDistance value="1.0000000000000000e+00"/>
    <ShowVolumeClippingBox value="0"/>
    <VolumeRenderingBounds value="-9.6000000000000000e+01 9.6000000000000000e+01 -1.3200000000000000e+02 9.6000000000000000e+01 -7.8000000000000000e+01 1.1400000000000000e+02 "/>
    <ScalarOpacity>
     <NbPoints value="2"/>
     <Point_0 value="0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </ScalarOpacity>
    <GradientOpacity>
     <NbPoints value="2"/>
     <Point_0 value="0.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <Point_1 value="2.5500000000000000e+02 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </GradientOpacity>
    <ColorTransferFunction>
     <NbColorPoints value="2"/>
     <ColorPoint_0 value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
     <ColorPoint_1 value="2.5500000000000000e+02 1.0000000000000000e+00 1.0000000000000000e+00 1.0000000000000000e+00 5.0000000000000000e-01 0.0000000000000000e+00 "/>
    </ColorTransferFunction>
   </ObjectInScene_8>
  </ObjectList>
  <Plugins>
   <USAcquisitionDoubleView/>
   <SEEGAtlas/>
  </Plugins>
  <SceneManager>
   <CurrentObjectID value="6"/>
   <ReferenceObjectID value="6"/>
   <ViewBackgroundColor value="0.0000000000000000e+00 0.0000000000000000e+00 4.9803921568627452e-01 "/>
   <View3DBackgroundColor value="0.0000000000000000e+00 0.0000000000000000e+00 4.9803921568627452e-01 "/>
   <Views>
    <NumberOfViews value="4"/>
    <View_0>
     <ViewID value="-2"/>
     <ViewType value="2"/>
     <Name value="Transverse"/>
     <Position value="5.0000000000000000e-01 -1.7500000000000000e+01 6.6678232545021535e+02 "/>
     <FocalPoint value="5.0000000000000000e-01 -1.7500000000000000e+01 1.8500000000000000e+01 "/>
     <Scale value="1.2393130285793180e+02"/>
     <ViewUp value="0.0000000000000000e+00 1.0000000000000000e+00 0.0000000000000000e+00 "/>
     <ViewAngle value="3.0000000000000000e+01"/>
    </View_0>
    <View_1>
     <ViewID value="-3"/>
     <ViewType value="3"/>
     <Name value="ThreeD"/>
     <Position value="1.0038195644853695e+03 0.0000000000000000e+00 0.0000000000000000e+00 "/>
     <FocalPoint value="0.0000000000000000e+00 0.0000000000000000e+00 0.0000000000000000e+00 "/>
     <Scale value="2.5980762113533160e+02"/>
     <ViewUp value="0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
     <ViewAngle value="3.0000000000000000e+01"/>
    </View_1>
    <View_2>
     <ViewID value="-4"/>
     <ViewType value="1"/>
     <Name value="Coronal"/>
     <Position value="5.0000000000000000e-01 -6.6578232545021535e+02 1.8500000000000000e+01 "/>
     <FocalPoint value="5.0000000000000000e-01 -1.7500000000000000e+01 1.8500000000000000e+01 "/>
     <Scale value="1.0831816237188875e+02"/>
     <ViewUp value="0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
     <ViewAngle value="3.0000000000000000e+01"/>
    </View_2>
    <View_3>
     <ViewID value="-5"/>
     <ViewType value="0"/>
     <Name value="Sagittal"/>
     <Position value="-6.4778232545021535e+02 -1.7500000000000000e+01 1.8500000000000000e+01 "/>
     <FocalPoint value="5.0000000000000000e-01 -1.7500000000000000e+01 1.8500000000000000e+01 "/>
     <Scale value="1.3312155220053992e+02"/>
     <ViewUp value="0.0000000000000000e+00 0.0000000000000000e+00 1.0000000000000000e+00 "/>
     <ViewAngle value="3.0000000000000000e+01"/>
    </View_3>
   </Views>
  </SceneManager>
  <AxesHidden value="0"/>
  <CursorVisible value="1"/>
  <CutPlanesCursorColor_r value="50"/>
  <CutPlanesCursorColor_g value="50"/>
  <CutPlanesCursorColor_b value="50"/>
  <QuadViewWindow>
   <CurrentViewWindow value="3"/>
   <ViewExpanded value="0"/>
  </QuadViewWindow>
  <Plugins>
   <GeneratedSurface/>
   <LabelVolumeToSurfaces/>
   <LandmarkRegistrationObject/>
   <PRISMVolumeRender/>
   <USAcquisitionDoubleView/>
   <SEEGAtlas/>
  </Plugins>
 </SaveScene>
</configuration>
    """)

    #Replace correspoding image names in the xml scene

    xml_modified = default_xml.substitute(
                        replace_brain_image_path = os.path.relpath(images_list['mr_object_in_oriented_space_masked'].scan, minc_dir),
                        replace_brain_image_name = images_list['mr_object_in_oriented_space_masked'].name,
                        replace_head_image_ct_path = os.path.relpath(images_list['ct_object_in_oriented_space'].scan, minc_dir),
                        replace_head_image_ct_name = images_list['ct_object_in_oriented_space'].name,
                        replace_head_image_mr_path = os.path.relpath(images_list['mr_object_in_oriented_space'].scan, minc_dir),
                        replace_head_image_mr_name = images_list['mr_object_in_oriented_space'].name,
                        )

    file_out = open(file_path, "wt")
    file_out.write(xml_modified)
    file_out.close()

def parse_options():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description='Preprocess images for seeg analysis')

    parser.add_argument("input_dir",
                        help="Input directory, it contains preimplantation MR and CT, "\
                         "and postimplantation CT DICOM directories")

    parser.add_argument("pre_imp_mr",
                        help="Name of the preimplantation MR DICOM directory, inside the input_dir.")

    parser.add_argument("post_imp_ct",
                        help="Name of the postimplantation CT DICOM directory, inside the input_dir.")

    parser.add_argument("subject",
                        help="Subject id")

    parser.add_argument("output_dir",
                        help="Output directory. It should exist.")

    options = parser.parse_args()

    return options

def create_dir(dir_path):
    """
    Create a directory.

    Arguments: dir_path Path of the directory to be created.
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def convert_files_to_minc(options, minc_dir, minc_pre_imp_mr_name, minc_post_imp_ct_name):
    """
    Convert DICOM files to minc.

    Arguments: options Dictionary containing the input directory and mr and ct DICOM image paths
               minc_dir Directory to store minc images
               minc_pre_imp_mr_name Name of the mr minc image
               minc_post_imp_ct_name Name of the ct minc image
    """
    pre_imp_mr_files = os.path.join(options.input_dir, options.pre_imp_mr, 'IM*')
    os.system('dcm2mnc ' + pre_imp_mr_files + ' ' + minc_dir + ' -anon' + ' -fname ' +
              minc_pre_imp_mr_name + ' -dname' + " ''")

    post_imp_ct_files = os.path.join(options.input_dir, options.post_imp_ct, 'IM*')
    os.system('dcm2mnc ' + post_imp_ct_files + ' ' + minc_dir + ' -anon' + ' -fname ' +
              minc_post_imp_ct_name + ' -dname' + " ''")

def register_rigid_ct_in_mr_space(minc_pre_imp_mr_path, minc_post_imp_ct_path, minc_post_imp_ct_reg_mr_path):
    """
    Rigidly register ct image in mr space.

    Arguments: minc_pre_imp_mr_path Path of the mr minc image
               minc_post_imp_ct_path Path of the ct minc image

    Results:   minc_post_imp_ct_path Path of the ct minc image registered in mr space.
    """
    temp_dir_register_rigid_ct_in_mr_space = 'temp_dir_register_rigid_ct_in_mr_space'
    os.system('mkdir ' + temp_dir_register_rigid_ct_in_mr_space)
    os.system('elastix -f ' + minc_pre_imp_mr_path + ' -m ' + minc_post_imp_ct_path + ' -out ' +
               temp_dir_register_rigid_ct_in_mr_space + ' -p ./test/parameters_register_ct_to_mr_rigid.txt')
    os.system('cp ' + temp_dir_register_rigid_ct_in_mr_space + '/result.0.mnc ' + minc_post_imp_ct_reg_mr_path)
    os.system('rm -rf ' + temp_dir_register_rigid_ct_in_mr_space)     

def register_mr_and_ct_in_oriented_space_no_scale(mr_object_intensity_normalized, ct_object_in_mr_space, mr_model, mr_object_in_oriented_space,
                                            ct_object_in_oriented_space):
    """
    Rigidly register ct image in mr space.

    Arguments: mr_object_intensity_normalized MR image, already preprocessed
               ct_object_in_mr_space CT image in tal space
               mr_model Model of tal space             

    Results:   mr_object_in_tal_space MR image in tal space.
               ct_object_in_tal_space CT image in tal space.
    """
    t1w_tal_par=MriAux(prefix=minc_dir, name=options.subject+'_tal_par_t1w')
    t1w_tal_log=MriAux(prefix=minc_dir, name=options.subject+'_tal_log_t1w_')
    mr_to_tal_transform = MriTransform(prefix=minc_dir, name=options.subject+'_mr_to_tal_transform')
    mr_to_oriented_transform_no_scale = MriTransform(prefix=minc_dir, name=options.subject+'_mr_to_oriented_transform_no_scale')
    mr_to_oriented_transform_unscale=MriTransform(prefix=minc_dir, name='mr_to_oriented_transform_unscale')
    mr_to_tal_transform_config = {"noscale":True, "type":"-lsq6", "objective":"-nmi"}   #Check this
 
    lin_registration(mr_object_intensity_normalized, mr_model, mr_to_tal_transform, parameters=mr_to_tal_transform_config,
                     par=t1w_tal_par, log=t1w_tal_log)  
    xfm_remove_scale(mr_to_tal_transform, mr_to_oriented_transform_no_scale, unscale=mr_to_oriented_transform_unscale)
    warp_scan(mr_object_intensity_normalized, mr_model, mr_object_in_oriented_space, transform=mr_to_oriented_transform_no_scale, 
            parameters=mr_to_tal_transform_config)
    warp_scan(ct_object_in_mr_space, mr_model, ct_object_in_oriented_space, transform=mr_to_oriented_transform_no_scale, 
            parameters=mr_to_tal_transform_config)

if __name__ == '__main__':
    options = parse_options()

    # Modify the lines below, depending on where the mr_model and beast are
    mr_model = MriScan(scan="/ipl/quarantine/models/icbm152_model_09c"+os.sep+"mni_icbm152_t1_tal_nlin_sym_09c"+'.mnc',
                     mask="/ipl/quarantine/models/icbm152_model_09c"+os.sep+"mni_icbm152_t1_tal_nlin_sym_09c"+'_mask.mnc')    
    beast_parameters = {"beastlib": "/ipl/quarantine/models/beast"}

    #Define all structures that are going to be used
    minc_dir = os.path.join(options.output_dir, options.subject)
    minc_pre_imp_mr_name = 'minc_pre_imp_mr'
    minc_post_imp_ct_name = 'minc_post_imp_ct'
    minc_pre_imp_mr_path = os.path.join(minc_dir, minc_pre_imp_mr_name + '.mnc')
    minc_post_imp_ct_path = os.path.join(minc_dir, minc_post_imp_ct_name + '.mnc')
    minc_post_imp_ct_reg_mr_path = os.path.join(minc_dir, minc_post_imp_ct_name + '_reg_mr' + '.mnc')
    mr_object = MriScan(prefix=minc_dir, name=options.subject+'_full_head_image',modality='t1w')
    ct_object_in_mr_space = MriScan(prefix=minc_dir, name=options.subject+'_full_head_image_mr_space',modality='ct')
    mr_object_denoised = MriScan(prefix=minc_dir, name=options.subject+'_full_head_image_denoised',modality='t1w')
    mr_object_field = MriScan(prefix=minc_dir, name=options.subject+'_full_head_image_field_nonuniformity_correction', modality='t1w', mask=None)
    mr_object_nonuniformity_corrected = MriScan(prefix=minc_dir, name=options.subject+'_full_head_image_nonuniformity_corrected', modality='t1w', mask=None)
    mr_object_intensity_normalized=MriScan(prefix=minc_dir, name=options.subject+'_full_head_image_intensity_normalized', modality='t1w', mask=None)
    mr_object_in_oriented_space = MriScan(prefix=minc_dir, name=options.subject+'_full_head_image_oriented_space',modality='t1w')
    mr_object_in_oriented_space_masked = MriScan(prefix=minc_dir, name=options.subject+'_brain_image_oriented_space',modality='t1w')
    ct_object_in_oriented_space = MriScan(prefix=minc_dir, name=options.subject+'_full_head_image_oriented_space',modality='ct')
    
    #Preprocess ct and mr images
    if not (os.path.exists(minc_dir)):
        create_dir(minc_dir)
    if not(os.path.exists(minc_pre_imp_mr_path) and os.path.exists(minc_post_imp_ct_path)):
        convert_files_to_minc(options, minc_dir, minc_pre_imp_mr_name, minc_post_imp_ct_name)
        os.system('cp ' +  minc_pre_imp_mr_path + ' ' + mr_object.scan)
    if not os.path.exists(mr_object_denoised.scan):
        denoise(mr_object, mr_object_denoised)
    if not os.path.exists(mr_object_field.scan):
        estimate_nu(mr_object_denoised, mr_object_field, model=mr_model)
    if not os.path.exists(mr_object_nonuniformity_corrected.scan):
        apply_nu(mr_object_denoised, mr_object_field, mr_object_nonuniformity_corrected)
    if not os.path.exists(mr_object_intensity_normalized.scan):
        normalize_intensity(mr_object_nonuniformity_corrected, mr_object_intensity_normalized, model=mr_model)
    if not os.path.exists(minc_post_imp_ct_reg_mr_path):
        register_rigid_ct_in_mr_space(minc_pre_imp_mr_path, minc_post_imp_ct_path, minc_post_imp_ct_reg_mr_path)
        os.system('cp ' +  minc_post_imp_ct_reg_mr_path + ' ' + ct_object_in_mr_space.scan)
    if not(os.path.exists(minc_post_imp_ct_reg_mr_path) and os.path.exists(mr_object_in_oriented_space.scan)):
        register_mr_and_ct_in_oriented_space_no_scale(mr_object_intensity_normalized, ct_object_in_mr_space, mr_model,
                                                mr_object_in_oriented_space, ct_object_in_oriented_space)  
    if not os.path.exists(mr_object_in_oriented_space_masked.scan):
        extract_brain_beast(mr_object_in_oriented_space, parameters=beast_parameters, model=mr_model)
        mincTools.command(['mincmask','-clobber',mr_object_in_oriented_space.scan,mr_object_in_oriented_space.mask,mr_object_in_oriented_space_masked.scan])

    images_list = dict()
    images_list["mr_object_in_oriented_space"] = mr_object_in_oriented_space
    images_list["ct_object_in_oriented_space"] = ct_object_in_oriented_space
    images_list["mr_object_in_oriented_space_masked"] = mr_object_in_oriented_space_masked                     
    
    save_scene(images_list, minc_dir, os.path.join(minc_dir, 'scene.xml')) 